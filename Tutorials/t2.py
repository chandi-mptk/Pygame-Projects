# Import Modules
import pygame
from pygame.locals import *

# Initialise Pygame (Get Hardware Details and Auto Configure)
pygame.init()

# Screen Size As Constant
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen Initialise
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Main Loop State Variable
running = True

# Main Loop
while running:

    # Events in Queue
    for event in pygame.event.get():

        # Check User Press Key
        if event.type == KEYDOWN:

            # Esc. Key to Quit
            if event.key == K_ESCAPE:
                running = False

        # Click Close Button
        elif event.type == QUIT:
            running = False

        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Create a surface and pass in a tuple containing its length and width
        surf = pygame.Surface((50, 50))

        # Give the surface a color to separate it from the background
        surf.fill((0, 0, 0))
        rect = surf.get_rect()

        # This line says "Draw surf onto the screen at the center"
        screen.blit(surf, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()

        # Put the center of surf at the center of the display
        surf_center = (
            (SCREEN_WIDTH - surf.get_width()) / 2,
            (SCREEN_HEIGHT - surf.get_height()) / 2
        )

        # Draw surf at the new coordinates
        screen.blit(surf, surf_center)
        pygame.display.flip()
