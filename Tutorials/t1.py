# Simple pygame program

# Import and initialize the pygame library
import pygame
from random import randint
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((500, 500))

# Set up Clock
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 500), randint(0, 500)),
                       randint(0, 75))

    # Flip the display
    pygame.display.flip()

    # Set Frame Rate to 60
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
