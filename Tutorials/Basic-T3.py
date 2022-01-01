import pygame

from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
)

pygame.init()

# Screen Dimension as Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Background Color
BG_COLOR = (255, 255, 255)

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set Title
pygame.display.set_caption("Pygame Tutorial 3 - Rectangle Box")

running = True
rect_color = (255, 0, 0)

while running:

    # Set Background Color
    screen.fill(BG_COLOR)

    # Get Event in Event's Que
    for event in pygame.event.get():

        # Check Any Key Press
        if event.type == KEYDOWN:

            # Check If the Pressed Key is Escape
            if event.key == K_ESCAPE:
                # Set Running as false to Exit
                running = False

        # Check Clos Button Clicked
        elif event.type == QUIT:

            # Set Running as false to Exit
            running = False

    pygame.draw.rect(screen, rect_color, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()
