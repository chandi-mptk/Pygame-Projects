import pygame
from random import choice

from pygame.locals import *

# Initialise Pygame
pygame.init()

# Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set Sync Clock & Frames Per Second(FPS)
clock = pygame.time.Clock()
FPS = 30

# Set Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set Screen
# SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Draw Shapes")
SCREEN.fill(WHITE)

# Screen Splitting Area Selection
SCREEN1 = pygame.Rect((0, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2))
SCREEN2 = pygame.Rect((SCREEN_WIDTH / 3, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2))
SCREEN3 = pygame.Rect((SCREEN_WIDTH * 2 / 3, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2))
SCREEN4 = pygame.Rect((0, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2))
SCREEN5 = pygame.Rect((SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2))
SCREEN6 = pygame.Rect((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2))

# Set The Area as Sub Frames
sub_scr1 = SCREEN.subsurface(SCREEN1)
sub_scr2 = SCREEN.subsurface(SCREEN2)
sub_scr3 = SCREEN.subsurface(SCREEN3)
sub_scr4 = SCREEN.subsurface(SCREEN4)
sub_scr5 = SCREEN.subsurface(SCREEN5)
sub_scr6 = SCREEN.subsurface(SCREEN6)

# Drawing a line on each split "screen" Vertical Lines Upper Portion
pygame.draw.line(sub_scr1, BLACK, (0, 0), (0, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr2, BLACK, (0, 0), (0, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr3, BLACK, (0, 0), (0, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr3, BLACK, (SCREEN_WIDTH / 3, 0), (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2), 10)

# Drawing a line on each split "screen" Vertical Lines Lower Portion
pygame.draw.line(sub_scr4, BLACK, (0, 0), (0, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr5, BLACK, (0, 0), (0, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr6, BLACK, (0, 0), (0, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr6, BLACK, (SCREEN_WIDTH / 3, 0), (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2), 10)

# Drawing a line on each split "screen" Horizontal Lines Upper Portion
pygame.draw.line(sub_scr1, BLACK, (0, 0), (SCREEN_WIDTH / 3, 0), 10)
pygame.draw.line(sub_scr2, BLACK, (0, 0), (SCREEN_WIDTH / 3, 0), 10)
pygame.draw.line(sub_scr3, BLACK, (0, 0), (SCREEN_WIDTH / 3, 0), 10)

# Drawing a line on each split "screen" Horizontal Lines Middle Portion
pygame.draw.line(sub_scr1, BLACK, (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr2, BLACK, (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2), 10)
pygame.draw.line(sub_scr3, BLACK, (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2), 10)

# Drawing a line on each split "screen" Horizontal Lines Bottom Portion
pygame.draw.line(sub_scr1, BLACK, (0, SCREEN_HEIGHT), (SCREEN_WIDTH / 3, SCREEN_HEIGHT), 10)
pygame.draw.line(sub_scr2, BLACK, (0, SCREEN_HEIGHT), (SCREEN_WIDTH / 3, SCREEN_HEIGHT), 10)
pygame.draw.line(sub_scr3, BLACK, (0, SCREEN_HEIGHT), (SCREEN_WIDTH / 3, SCREEN_HEIGHT), 10)

# Shapes to draw
pygame.draw.polygon(sub_scr1, RED, [(50, 50), (100, 120), (150, 150), (200, 240), (250, 250)])
pygame.draw.line(sub_scr2, GREEN, (100, 30), (230, 170), width=5)
pygame.draw.line(sub_scr3, BLUE, (230, 170), (100, 130), width=5)
pygame.draw.circle(sub_scr4, RED, (100, 150), 30)
pygame.draw.ellipse(sub_scr5, GREEN, (50, 50, 200, 100))
pygame.draw.rect(sub_scr6, BLUE, (100, 200, 100, 50), 2)

running = True

while running:
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    clock.tick(FPS)
