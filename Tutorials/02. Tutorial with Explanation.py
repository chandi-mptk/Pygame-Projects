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


SCREEN_DIMENSION = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

# Above Instruction Sets Screen Dimension (Screen width and Screen Height) Constant values.

DISPLAY_SURF = pygame.display.set_mode(SCREEN_DIMENSION, 0, 32)

# set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
# Above Instruction is a call to the pygame.display.set_mode() function, which returns the pygame.Surface object
# for the window. Notice that we pass a tuple value of two integers in SCREEN_DIMENSION Constant to the function.
# This tuple tells the set_mode() function how wide and how high to make the window in pixels.
# (400, 300) will make a window with a width of 400 pixels and height of 300 pixels.

pygame.display.set_caption('Drawing')

# Above Instruction sets the caption text that will appear at the top of the window by calling the
# pygame.display.set_caption() function. The string value 'Hello World!' is passed in this function call
# to make that text appear as the caption:

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Above Instructions - There are three primary colors of light: red, green and blue.
# (Red, blue, and yellow are the primary colors for paints and pigments, but the computer monitor uses light, not paint)
# By combining different amounts of these three colors you can form any other color.
# In Pygame, we represent colors with tuples of three integers. The first value in the tuple is how much red is
# in the color. An integer value of 0 means there is no red in this color, and a value of 255 means there is the
# maximum amount of red in the color. The second value is for green and the third value is for blue.
# These tuples of three integers used to represent a color are often called RGB values.

DISPLAY_SURF.fill(WHITE)

# fill(color) – The fill() method is not a function but a method of pygame.Surface objects.
# It will completely fill in the entire Surface object with whatever color value you pass as for the color parameter.

polygon_sides = [(146, 0), (291, 106), (236, 277), (56, 277), (0, 106)]

pygame.draw.polygon(DISPLAY_SURF, GREEN, polygon_sides)

# pygame.draw.polygon(surface, color, pointlist, width) – A polygon is shape made up of only flat sides.
# The surface and color parameters tell the function on what surface to draw the polygon, and what color to make it.
# The pointlist parameter is a tuple or list of points (ie. tuple or list of two-integer tuples for XY coordinates).
# The polygon is drawn by drawing lines between each point and the point that comes after it in the tuple.
# Then a line is drawn from the last point to the first point. You can also pass a list of points instead of a
# tuple of points. The width parameter is optional. If you leave it out, the polygon that is drawn will be filled in.
# If you do pass an integer value for the width parameter, only the outline of the polygon will be drawn.
# The integer represents how many pixels width the polygon’s outline will be. Passing 1 for the width parameter
# will make a skinny polygon, while passing 4 or 10 or 20 will make thicker polygons. If you pass the integer 0
# for the width parameter, the polygon will be filled in. All of the pygame.draw drawing functions have optional
# width parameters at the end, and they work the same way as pygame.draw.polygon()’s width parameter.
# Probably a better name for the width parameter would have been thickness, since that parameter controls how thick
# the lines you draw are.

pygame.draw.line(DISPLAY_SURF, BLUE, (60, 60), (120, 60), 4)

# pygame.draw.line(surface, color, start_point, end_point, width) – This function draws a line between the
# start_point and end_point parameters.

pygame.draw.line(DISPLAY_SURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAY_SURF, BLUE, (60, 120), (120, 120), 4)

# pygame.draw.lines(surface, color, closed, pointlist, width) – This function draws a series of lines
# from one point to the next, much like pygame.draw.polygon(). The only difference is that if you pass
# False for the closed parameter, there will not be a line from the last point in the pointlist parameter to the
# first point. If you pass True, then it will draw a line from the last point to the first.

pygame.draw.circle(DISPLAY_SURF, BLUE, (300, 50), 20, 0)

# pygame.draw.circle(surface, color, center_point, radius, width) – This function draws a circle.
# The center of the circle is at the center_point parameter. The integer passed for the radius parameter
# sets the size of the circle.
# The radius of a circle is the distance from the center to the edge. Passing 20 for the radius parameter
# will draw a circle that has a radius of 20 pixels.

pygame.draw.ellipse(DISPLAY_SURF, RED, (300, 250, 40, 80), 1)

# pygame.draw.ellipse(surface, color, bounding_rectangle, width) – This function draws an ellipse This function has
# all the usual parameters, but in order to tell the function how large and where to draw the ellipse, you must
# specify the bounding rectangle of the ellipse. A bounding rectangle is the smallest rectangle that can be drawn
# around a shape.

pygame.draw.rect(DISPLAY_SURF, RED, (200, 150, 100, 50))

# pygame.draw.rect(surface, color, rectangle_tuple, width) – This function draws a rectangle.
# The rectangle_tuple is either a tuple of four integers (for the XY coordinates of the top left corner,
# and the width and height) or a pygame.Rect object can be passed instead. If the rectangle_tuple has the
# same size for the width and height, a square will be drawn.

pixObj = pygame.PixelArray(DISPLAY_SURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# pygame.PixelArray Objects
# To set the color of a single Pixel pygame.PixelArray object of a Surface object is used.
# Creating a PixelArray object of a Surface object will “lock” the Surface object. While a Surface object is locked,
# the drawing functions can still be called on it, but it cannot have images like PNG or JPG images drawn on it
# with the blit() method. If you want to see if a Surface object is locked, the get_locked() Surface method will return
# True if it is locked and False if it is not. The PixelArray object that is returned from pygame.PixelArray()
# can have individual pixels set by accessing them with two indexes. For example, pixObj[480][380] = BLACK will set
# the pixel at X coordinate 480 and Y coordinate 380 to be black. To tell Pygame that you are finished drawing
# individual pixels, delete the PixelArray object with a del statement. Deleting the PixelArray object will “unlock”
# the Surface object so that you can once again draw images on it. If you forget to delete the PixelArray object,
# the next time you try to blit (that is, draw) an image to the Surface the program will raise an error that says,
# “pygame.error: Surfaces must not be locked during blit”.

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
