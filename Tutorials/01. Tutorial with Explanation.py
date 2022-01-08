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

# Above Instruction is a call to the pygame.display.set_mode() function, which returns the pygame.Surface object
# for the window. Notice that we pass a tuple value of two integers in SCREEN_DIMENSION Constant to the function.
# This tuple tells the set_mode() function how wide and how high to make the window in pixels.
# (400, 300) will make a window with a width of 400 pixels and height of 300 pixels.

pygame.display.set_caption('Hello World!')

# Above Instruction sets the caption text that will appear at the top of the window by calling the
# pygame.display.set_caption() function. The string value 'Hello World!' is passed in this function call
# to make that text appear as the caption:

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

        pygame.display.update()

        # Above Instruction calls the pygame.display.update() function, which draws the Surface object returned by
        # pygame.display.set_mode() to the screen (remember we stored this object in the DISPLAYSURF variable).
        # Since the Surface object hasn’t changed, the same black image is redrawn to the screen each time
        # pygame.display.update() is called.
