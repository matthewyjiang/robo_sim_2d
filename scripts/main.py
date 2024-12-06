#!/usr/bin/env python

import pygame
from robo_sim_2d.robot import Robot
import numpy
import rospy

from robo_sim_2d.srv import AddRobot, AddRobotResponse, ApplyForceForward, ApplyForceForwardResponse

entities = {}
texts = []

def add_robot(req):
    global entities
    robot_name = req.robot_name
    entities[robot_name] = Robot(req.x, req.y, req.mass, 0.5)
    return AddRobotResponse(True, "Robot {robot_name} added")

def apply_force_forward(req):
    global entities
    robot_name = req.robot_name
    force = req.force
    if robot_name in entities:
        entities[robot_name].add_force_in_theta_direction(force)
        return AddRobotResponse(True, "Force applied to {robot_name}")
    else:
        return AddRobotResponse(False, "Robot {robot_name} not found")

def update_game():

    # Update all entities
    for entity in entities.values():
        entity.update(1/60.0)


def main():
    
    rospy.init_node('main', anonymous=True)
    rate = rospy.Rate(60)
    
    add_robot_service = rospy.Service('add_robot', AddRobot, add_robot)
    apply_force_forward_service = rospy.Service('apply_force_forward', ApplyForceForward, apply_force_forward)
    
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Robo Sim 2D")

    # print robot coordinates using draw text
    font = pygame.font.SysFont(None, 36)

    # Run the game loop
    clock = pygame.time.Clock()
    while not rospy.is_shutdown():
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update the game
        update_game()

        # Draw the entities
        screen.fill((255, 255, 255))
        for entity in entities.values():
            entity.draw(screen)
            texts.append((font.render(f"{entity.get_coordinates()}", True, (0, 0, 0)), (0, 0)))
        
        texts.clear()
        
        
        for text, textpos in texts:
            screen.blit(text, textpos)

        # Update the display
        pygame.display.flip()

        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    

