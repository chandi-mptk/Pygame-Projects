import pygame

# Above Instruction is a simple import statement that imports the pygame modules
# so that our program can use the functions in them.
# All the Pygame functions dealing with graphics, sound, and other features
# that Pygame provides are in the pygame module.

from pygame.locals import *

# Above Instruction is also an import statement. However, instead of the import modulename format,
# it uses the from modulename import * format. Normally if you want to call a function
# that is in a module, you must use the modulename. functionname() format after importing the module.
# However, with from modulename import *, you can skip the modulename.
# portion and simply use functionname() (just like Python’s built-in functions).

pygame.init()

# Above Instruction is the pygame.init() function call, which always needs to be called after
# importing the pygame module and before calling any other Pygame function.
# You don’t need to know what this function does, you just need to know that it needs to be called first
# in order for many Pygame functions to work. If you ever see an error message like
# pygame.error: font not initialized, check to see if you forgot to call pygame.init() at the start of your program.

FPS = 30

# The frame rate or refresh rate is the number of pictures that the program draws per second,
# and is measured in FPS or frames per second. (On computer monitors, the common name for FPS is hertz.
# Many monitors have a frame rate of 60 hertz, or 60 frames per second.) A low frame rate in video games can make
# the game look choppy or jumpy. If the program has too much code to run to draw to the screen frequently enough,
# then the FPS goes down. But the games hear are simple enough that this won’t be issue even on old computers.

clock = pygame.time.Clock()

# A pygame.time.Clock object can help us make sure our program runs at a certain maximum FPS.
# This Clock object will ensure that our game programs don’t run too fast by putting in small pauses on each
# iteration of the game loop. If we didn’t have these pauses, our game program would run as fast as the
# computer could run it. This is often too fast for the player, and as computers get faster they would run
# the game faster too. A call to the tick() method of a Clock object in the game loop can make sure the game runs
# at the same speed no matter how fast of a computer it runs on.

SCREEN_DIMENSION = SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300

# Above Instruction Sets Screen Dimension (Screen width and Screen Height) Constant values.

DISPLAY_SURF = pygame.display.set_mode(SCREEN_DIMENSION, 0, 32)

# set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
# Above Instruction is a call to the pygame.display.set_mode() function, which returns the pygame.Surface object
# for the window. Notice that we pass a tuple value of two integers in SCREEN_DIMENSION Constant to the function.
# This tuple tells the set_mode() function how wide and how high to make the window in pixels.
# (400, 300) will make a window with a width of 400 pixels and height of 300 pixels.

pygame.display.set_caption('Animation')

# Above Instruction sets the caption text that will appear at the top of the window by calling the
# pygame.display.set_caption() function. The string value 'Hello World!' is passed in this function call
# to make that text appear as the caption:

WHITE = (255, 255, 255)

# Above Instructions - There are three primary colors of light: red, green and blue.
# (Red, blue, and yellow are the primary colors for paints and pigments, but the computer monitor uses light, not paint)
# By combining different amounts of these three colors you can form any other color.
# In Pygame, we represent colors with tuples of three integers. The first value in the tuple is how much red is
# in the color. An integer value of 0 means there is no red in this color, and a value of 255 means there is the
# maximum amount of red in the color. The second value is for green and the third value is for blue.
# These tuples of three integers used to represent a color are often called RGB values.

catImg = pygame.image.load('Images/cat.png')

# The image of the cat was stored in a file named cat.png in Images Folder. To load this file’s image,
# the string 'Images/cat.png' is passed to the pygame.image.load() function. The pygame.image.load() function call
# will return a Surface object that has the image drawn on it. This Surface object will be a separate Surface object
# from the display Surface object, so we must blit (that is, copy) the image’s Surface object to the
# display Surface object. Blitting is drawing the contents of one Surface onto another. It is done with the
# blit() Surface object method.

cat_x = 10
cat_y = 10

direction = 'right'

# Variables store the initial Position and Direction of the image

running = True

# Set a variable to run the main loop

while running:
    # Above Instruction is a while loop that has a condition of True. This means that it never exits
    # till the running variable sets to False.

    # A game loop (also called a main loop) is a loop where the code does three things:
    # 1.      Handles events.
    # 2.      Updates the game state.
    # 3.      Draws the game state to the screen.
    for event in pygame.event.get():
        # pygame.event.Event Objects - Any time the user does one of several actions such as pressing a keyboard key or
        # moving the mouse on the program’s window, a pygame.event.Event object is created by the Pygame library
        # to record this “event”. (This is a type of object called Event that exists in the event module,
        # which itself is in the pygame module.) We can find out which events have happened by calling the
        # pygame.event.get() function, which returns a list of pygame.event.Event objects
        # (which we will just call Event objects for short).

        # Above Instruction is a for loop that will iterate over the list of Event objects that was returned by
        # pygame.event.get(). On each iteration through the for loop, a variable named event will be assigned the
        # value of the next event object in this list. The list of Event objects returned from pygame.event.get()
        # will be in the order that the events happened. If the user clicked the mouse and then pressed a keyboard key,
        # the Event object for the mouse click would be the first item in the list and the Event object for the
        # keyboard press would be second. If no events have happened, then pygame.event.get() will return a blank list.

        if event.type == QUIT:
            # Event objects have a member variable (also called attributes or properties) named type which tells us
            # what kind of event the object represents. Pygame has a constant variable for each of possible types
            # in the pygame.locals modules.

            # Above Instruction checks if the Event object’s type is equal to the constant QUIT.
            # Remember that since we used the from pygame.locals import * form of the import statement,
            # we only have to type QUIT instead of pygame.locals.QUIT.

            running = False

            # If The Quit instruction receives then by setting the running variable to False
            # The loop as well as The Script will exit

    DISPLAY_SURF.fill(WHITE)

    # fill(color) – The fill() method is not a function but a method of pygame.Surface objects. It will completely
    # fill in the entire Surface object with whatever color value you pass as for the color parameter.

    # Every FPS this animation Starts
    if direction == 'right':
        cat_x += 5

        # At Start Right is the direction until the position of x reaches the right most corner
        # (Left top side is 120 pixels(the width of image) away from right border)

        if cat_x == SCREEN_WIDTH - 120:

            # The image Changes the Direction
            direction = 'down'
    elif direction == 'down':
        cat_y += 5

        # Moves up to the bottom of the screen
        # (Left top side is 80 pixels(the height of image) away from bottom border)

        if cat_y == SCREEN_HEIGHT - 80:

            # The image Changes the Direction
            direction = 'left'
    elif direction == 'left':
        cat_x -= 5

        # Moves up to the Left of the screen
        # (Left top side is 10 pixels away from Left border)

        if cat_x == 10:

            # The image Changes the Direction
            direction = 'up'
    elif direction == 'up':
        cat_y -= 5

        # Moves Up to the Top of the screen
        # (Left top side is 10 pixels away from Top border)
        if cat_y == 10:

            # The image Changes the Direction
            direction = 'right'

    DISPLAY_SURF.blit(catImg, (cat_x, cat_y))

    # Above Code of the animation program uses the blit() method to copy catImg to DISPLAY_SURF.
    # There are two parameters for blit(). The first is the source Surface object, which is what will be copied
    # onto the DISPLAY_SURF Surface object. The second parameter is a two-integer tuple for the X and Y values
    # of the topleft corner where the image should be blitted to.
    # If cat_x and cat_y were set to 100 and 200 and the width of catImg was 125 and the height was 79,
    # this blit() call would copy this image onto DISPLAY_SURF so that the top left corner of the catImg was
    # at the XY coordinate (100, 200) and the bottom right corner’s XY coordinate was at (225, 279).
    # Note that you cannot blit to a Surface that is currently “locked”
    # (such as when a PixelArray object has been made from it and not yet been deleted.)
    # The rest of the game loop is just changing the cat_x, cat_y, and direction variables so that the
    # cat moves around the window.

    pygame.display.update()

    # Above Instruction calls the pygame.display.update() function, which draws the Surface object returned by
    # pygame.display.set_mode() to the screen (remember we stored this object in the DISPLAYSURF variable).
    # Since the Surface object hasn’t changed, the same black image is redrawn to the screen each time
    # pygame.display.update() is called.

    clock.tick(FPS)

    # The Clock object’s tick() method should be called at the very end of the game loop, after the call to
    # pygame.display.update(). The length of the pause is calculated based on how long it has been since the
    # previous call to tick(), which would have taken place at the end of the previous iteration of the game loop.
    # (The first time the tick() method is called, it doesn’t pause at all.)
