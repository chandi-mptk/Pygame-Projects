import time

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

SCREEN_DIMENSION = SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300

# Above Instruction Sets Screen Dimension (Screen width and Screen Height) Constant values.

DISPLAY_SURF = pygame.display.set_mode(SCREEN_DIMENSION)

# set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
# Above Instruction is a call to the pygame.display.set_mode() function, which returns the pygame.Surface object
# for the window. Notice that we pass a tuple value of two integers in SCREEN_DIMENSION Constant to the function.
# This tuple tells the set_mode() function how wide and how high to make the window in pixels.
# (400, 300) will make a window with a width of 400 pixels and height of 300 pixels.

pygame.display.set_caption('Playing Sounds')

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

soundObj = pygame.mixer.Sound('Sounds/614138__josefpres__bass-loops-020-with-drums-long-loop-120-bpm.wav')
# Playing sounds that are stored in sound files is even simpler than displaying images from image files.
# First, you must create a pygame.mixer.Sound object (which we will call Sound objects for short)
# by calling the pygame.mixer.Sound() constructor function. It takes one string parameter, which is the filename
# of the sound file. Pygame can load WAV, MP3, or OGG files.

# Loading and playing background music:

pygame.mixer.music.load('Sounds/Monkeys-Spinning-Monkeys.mp3')

# The Sound objects are good for sound effects to play when the player takes damage, slashes a sword,
# or collects a coin. But your games might also be better if they had background music playing regardless of
# what was going on in the game. Pygame can only load one music file to play in the background at a time.
# To load a background music file, call the pygame.mixer.music.load() function and pass it a string argument of
# the sound file to load. This file can be WAV, MP3, or MIDI format.

pygame.mixer.music.play(-1, 0.0)

# To begin playing the loaded sound file as the background music, call the pygame.mixer.music.play(-1, 0.0) function
# The -1 argument makes the background music forever loop when it reaches the end of the sound file.
# If you set it to an integer 0 or larger, then the music will only loop that number of times instead of
# looping forever. The 0.0 means to start playing the sound file from the beginning. If you pass
# a larger integer or float, the music will begin playing that many seconds into the sound file.
# For example, if you pass 13.5 for the second parameter, the sound file with begin playing at the
# point 13.5 seconds in from the beginning.

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

    pygame.display.update()

    # Above Instruction calls the pygame.display.update() function, which draws the Surface object returned by
    # pygame.display.set_mode() to the screen (remember we stored this object in the DISPLAYSURF variable).
    # Since the Surface object hasn’t changed, the same black image is redrawn to the screen each time
    # pygame.display.update() is called.

    soundObj.play()

    # To play this sound, call the Sound object’s play() method.

    time.sleep(1)
    # The program execution continues immediately after play() is called;
    # it does not wait for the sound to finish playing before moving on to the next line of code.

    soundObj.stop()

    # If you want to immediately stop the Sound object from playing call the stop() method.
    # The stop() method has no arguments.

pygame.mixer.music.stop()
# To stop playing the background music immediately, call the pygame.mixer.music.stop() function.
# This function has no arguments.


