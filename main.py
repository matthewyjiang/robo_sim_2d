import pygame
import robot
import numpy

entities = []
texts = []

def update_game():

    # Update all entities
    for entity in entities:
        entity.update(dt=1/60)


def main():
    # Initialize pygame
    pygame.init()

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
        
        texts.clear()
        
        
        for text, textpos in texts:
            screen.blit(text, textpos)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
    

