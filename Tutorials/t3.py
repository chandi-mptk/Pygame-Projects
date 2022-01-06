# Imports
import random
import time

import pygame
from pygame.locals import *

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
CLOCK = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

# Create a white screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/missile.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/jet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        # Disappear in Left and Appear in Right when going Out of Screen
        else:
            self.rect.right = SCREEN_WIDTH - 1
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        # Disappear in Right and Appear in Left when going Out of Screen
        else:
            self.rect.left = 1


# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
running = True

while running:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == INC_SPEED:
            SPEED += 1

    SCREEN.fill(WHITE)

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        SCREEN.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        SCREEN.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        running = False

    pygame.display.update()
    CLOCK.tick(FPS)
