# Import Modules
import pygame
from random import randint

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Screen Size As Constant
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Images/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(0, SCREEN_HEIGHT / 2))

    # Move the sprite based on user key presses
    def update(self, pressed_key):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -15)
            # move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 15)
            # move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-15, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(15, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < SCREEN_HEIGHT // 4:
            self.rect.top = SCREEN_HEIGHT // 4
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                randint(SCREEN_HEIGHT // 4, SCREEN_HEIGHT)
            )
        )
        self.speed = randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                randint(0, SCREEN_HEIGHT // 4)
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Initialise Pygame (Get Hardware Details and Auto Configure)
pygame.init()

# Set up the clock for a decent frame rate
clock = pygame.time.Clock()

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
# pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
# collision_sound = pygame.mixer.Sound("Collision.ogg")

# Screen Initialise
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

        # Add a new enemy?
        elif event.type == ADD_ENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new Cloud
        elif event.type == ADD_CLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user key presses
        player.update(pressed_key=pressed_keys)

        # Update enemy position
        enemies.update()
        clouds.update()

        # Fill the screen with sky blue
        screen.fill((135, 206, 250))

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # Stop any moving sounds and play the collision sound
            # move_up_sound.stop()
            # move_down_sound.stop()
            # collision_sound.play()

            # If so, then remove the player and stop the loop
            player.kill()
            running = False

        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)

# All done! Stop and quit the mixer.
pygame.mixer.music.stop()
pygame.mixer.quit()
