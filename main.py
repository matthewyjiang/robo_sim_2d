import pygame
import robot
import numpy

entities = []
texts = []

my_robot = robot.Robot(x=250, y=250, mass=10, friction=0.5)

error = 0
integral = 0
target = 750
last_error = 0

def update_game():
    dt=1/60
    global error
    global last_error
    global integral
    kP = 5
    kI = 0.01
    kD = 15
    # pid controller
    x = my_robot.get_coordinates()[0]
    error = target - x
    derivative = (error-last_error)/dt
    integral += error*dt
    
    numpy.clip(integral, -1000, 1000)
    
    output = kP*error+kD*derivative+kI*integral
    
    
    my_robot.add_force_in_theta_direction(output)
    
    last_error = error
    
    # Update all entities
    for entity in entities:
        entity.update(dt=1/60)


def main():
    # Initialize pygame
    pygame.init()

    entities.append(my_robot)

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Robo Sim 2D")

    # print robot coordinates using draw text
    font = pygame.font.SysFont(None, 36)

    # Run the game loop
    clock = pygame.time.Clock()
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update the game
        update_game()

        # Draw the entities
        screen.fill((255, 255, 255))
        for entity in entities:
            entity.draw(screen)

        # Get robot coordinates
        robot_x = my_robot.get_coordinates()[0]
        
        texts.clear()

        # Render text
        text = font.render("Robot X:" + str(robot_x),  1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = 100
        textpos.centery = 20
        
        # Render text
        text1 = font.render("Robot Error:" + str(error),  1, (10, 10, 10))
        textpos1 = text1.get_rect()
        textpos1.centerx = 100
        textpos1.centery = 60
        
        texts.append((text, textpos))
        texts.append((text1, textpos1))


        # Draw vertical line
        pygame.draw.line(screen, (0, 0, 0), (750, 0), (750, 600), 2)

        
        
        for text, textpos in texts:
            screen.blit(text, textpos)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
    

