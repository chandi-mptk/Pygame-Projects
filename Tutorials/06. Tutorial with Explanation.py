# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

# Import Modules
import pygame
import random

from pygame.locals import *

# Declair Global Modules
global CLOCK, DISPLAY_SURF

FPS = 30  # frames per second, the general speed of the program
WINDOW_WIDTH = 640  # size of window's width in pixels
WINDOW_HEIGHT = 480  # size of windows' height in pixels
REVEAL_SPEED = 8  # speed boxes' sliding reveals and covers
BOX_SIZE = 40  # size of box height & width in pixels
GAP_SIZE = 10  # size of gap between boxes in pixels
BOARD_WIDTH = 10  # number of columns of icons
BOARD_HEIGHT = 7  # number of rows of icons

# Check Every Box in the Screen has a Pair (Total Number of Boxes are Even)
assert (BOARD_WIDTH * BOARD_HEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

# X_MARGIN The balance Space after game area (Left & Right Margin) after Boxes arranged
X_MARGIN = int((WINDOW_WIDTH - (BOARD_WIDTH * (BOX_SIZE + GAP_SIZE))) / 2)

# Y_MARGIN The balance Space after game area (Top & Bottom Margin) after Boxes arranged
Y_MARGIN = int((WINDOW_HEIGHT - (BOARD_HEIGHT * (BOX_SIZE + GAP_SIZE))) / 2)

#        R    G    B
GRAY = (100, 100, 100)
NAVY_BLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Assign Colours to Game Screen Part Names
BG_COLOR = NAVY_BLUE
LIGHT_BG_COLOR = GRAY
BOX_COLOR = WHITE
HIGHLIGHT_COLOR = BLUE

# Shape Names To Variables
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# All Available Colors for Shapes as Tuple
ALL_COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)

# All Available Shapes as Tuples
ALL_SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

# Assure All Color Shape Combinations are able to set in pairs in the game board
assert len(ALL_COLORS) * len(
    ALL_SHAPES) * 2 >= BOARD_WIDTH * BOARD_HEIGHT, "Board is too big for the number of shapes/colors defined."


# Main Function of Game
def main():
    # Clock and Display Surface as Global Variable to access from every funcrion
    global CLOCK, DISPLAY_SURF

    # Initiate Pygame
    pygame.init()

    # Set Clock Object for Controlling Frame Rate of the Game
    CLOCK = pygame.time.Clock()

    # Set Game Surface
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    mouse_x = 0  # used to store x coordinate of mouse event
    mouse_y = 0  # used to store y coordinate of mouse event

    # Game Window Title
    pygame.display.set_caption('Memory Game')

    # Get a List of List of Tuples
    # List of Columns whose elements are shape, color tuple
    mainBoard = getRandomizedBoard()

    # List of List Which denote th reveal Status(Is box is open or not) in "True" or "False"
    # [[False, False, False, False, False, False, False],....]
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None  # stores the (x, y) of the first box clicked.

    # Give Color To Background
    DISPLAY_SURF.fill(BG_COLOR)

    # Animated Preview of hidden Icons by 8 at a time reveling is by a sliding the cover Animation
    startGameAnimation(mainBoard)

    # Main Loop Status variable
    running = True

    while running:  # main game loop
        # Mouse click Status Variable
        mouseClicked = False

        DISPLAY_SURF.fill(BG_COLOR)  # drawing the window
        # Draw mainBoard and as revealedBoxes status show or hide the icon
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():  # event handling loop
            # Detect Exit
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                running = False
            # Get mouse position Continuously
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            # Get mouse coordinates Where mouse click released
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                # Set Mouse Click Status Variable
                mouseClicked = True
        # Get box row column numbers from mouse coordinates
        boxx, boxy = getBoxAtPixel(mouse_x, mouse_y)
        # If Mouse is on any Box
        if boxx is not None and boxy is not None:
            # If the reveal Status is False (For Highlight only)
            if not revealedBoxes[boxx][boxy]:
                # High Light box Drawn (Blue Square around the box)
                drawHighlightBox(boxx, boxy)
            # If the reveal Status is False and Mouse clicked (For Open Box)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                # Show Icon with Box Cover Sliding Animation
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True  # set the box as "revealed"
                if firstSelection is None:  # the current box was the first box clicked
                    # Set By First Box Row Column values
                    firstSelection = (boxx, boxy)
                else:  # the current box was the second box clicked
                    # Get Shape and Color of First Icon
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    # Get Shape and Color of Secon Icon
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000)  # 1000 milliseconds = 1 sec
                        # Send the main board and list of Tuple Coordinates to be disabled(both box1 and box2)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        # Reset Reveal status to False of Both boxes
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    # If both Icons are Matching Check Game Completed?
                    elif hasWon(revealedBoxes):  # check if all pairs found
                        # All Pairs Found Victory Animation
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset the board for play Again
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        startGameAnimation(mainBoard)
                    firstSelection = None  # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        CLOCK.tick(FPS)


# A List of list (list of columns whose elements are the box status)
def generateRevealedBoxesData(val):
    # Set a blank list to append lists
    revealedBoxes = []
    # Iterate the column index
    for i in range(BOARD_WIDTH):
        # Insert a list whose value is the state of the box representing the
        # column of "i" and the row of the list index
        revealedBoxes.append([val] * BOARD_HEIGHT)
    # Return the List of List
    return revealedBoxes


# Create Game Board
def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []

    # This nested loop will set all possible shape, color combination tuple in icon list
    for color in ALL_COLORS:
        for shape in ALL_SHAPES:
            icons.append((shape, color))

    random.shuffle(icons)  # randomize the order of the icons list
    numIconsUsed = int(BOARD_WIDTH * BOARD_HEIGHT / 2)  # calculate how many icons are needed (Get half of Board Size)
    icons = icons[:numIconsUsed] * 2  # make two of each Icon(To make pairs)
    random.shuffle(icons)  # Shuffle the list to randomise the pairs

    # Create the board data structure, with randomly placed icons.
    board = []
    # Iterate through Column Number
    for x in range(BOARD_WIDTH):
        # Create a blank Column List
        column = []
        # Iterate through Row Number
        for y in range(BOARD_HEIGHT):
            # Append first Icon of the List generated Above added to column list in every row number
            column.append(icons[0])
            del icons[0]  # remove the icons from the list as we assign them in column list
        # Assign the column list as an element in the board list (List of Lists)
        board.append(column)
    # Return The board which contain a list of columns and its elements are the tuple of shape and Tuple for color
    # [[('lines', (255, 128, 0)), ('oval', (255, 128, 0)), ...],[('diamond', (255, 0, 255)),...], ...]
    return board


def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    # Game Screen is from Left to right X_MARGIN, first BOX_SIZE, GAP_SIZE,second BOX_SIZE so on and X_MARGIN
    left = boxx * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    # Game Screen is from Top to Bottom Y_MARGIN, first BOX_SIZE, GAP_SIZE,second BOX_SIZE so on and Y_MARGIN
    top = boxy * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    # By the equation We will Get the xth column yth row box's left Top coordinate
    return left, top


def getBoxAtPixel(x, y):
    # Iterate through box Column numbers
    for boxx in range(BOARD_WIDTH):
        # Iterate through box row numbers
        for boxy in range(BOARD_HEIGHT):
            # Get the left, top pixels of current box
            left, top = leftTopCoordsOfBox(boxx, boxy)
            # set the rectangle of current box
            boxRect = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            # By collide function Check Clicked on current box or not
            if boxRect.collidepoint(x, y):
                # If Clicked on Current box Return the box row, column numbers
                return boxx, boxy
    # Not clicked on box Return None
    return None, None


def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOX_SIZE * 0.25)  # syntactic sugar
    half = int(BOX_SIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy)  # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        # for Circle Center Point as pixels in tuple and radios is required
        # To get the center point of the Square left Pixel value + Half size of the box
        # and Top Pixel Value + Half size of the Squire
        # Radios is less than 5 Pixel of Half of the Box (Circle will cover 5 pixel inside from the sides)
        pygame.draw.circle(DISPLAY_SURF, color, (left + half, top + half), half - 5)
        # Center Hole is created by another Circle, the center point is same but
        # the radios is 5 Pixel less than quarter of the box and fill background color to show it as a hole
        pygame.draw.circle(DISPLAY_SURF, BG_COLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        # The Square is Half of the box height and half of the box width
        # Initial coordinates quarter below the top and quarter right from the box's respective sides
        # Height and width of the box is half of the box dimensions
        pygame.draw.rect(DISPLAY_SURF, color, (left + quarter, top + quarter, BOX_SIZE - half, BOX_SIZE - half))
    elif shape == DIAMOND:
        # Diamond is a square in different orientation but to draw that we need to use polygon function
        # every corner of the diamond is in center of every side of the box
        diamond_sides = ((left + half, top),  # Top side of the Box
                         (left + BOX_SIZE - 1, top + half),  # Right side of the box (BOX_SIZE - 1 set point in the box)
                         (left + half, top + BOX_SIZE - 1),  # Bottom Side of the box (BOX_SIZE - 1 set point in box)
                         (left, top + half)  # Left Side of the box
                         )
        pygame.draw.polygon(DISPLAY_SURF, color, diamond_sides)
    elif shape == LINES:
        # Draw Diagonal Lines in a 4 pixel gap and parallel to each other
        for i in range(0, BOX_SIZE, 4):
            # This first line starts from Left Top Corner to center
            # Eg. i = 0 - a dot on left top corner ((left, top), (left, top))
            # Eg. i = BOX_SIZE a line from left bottom to top Right ((left, bottom),(right, top))
            # bottom = top + BOX_SIZE and right = left + BOX_SIZE
            pygame.draw.line(DISPLAY_SURF, color, (left, top + i), (left + i, top))
            # This line tarts from Bottom Center to Right Corner
            pygame.draw.line(DISPLAY_SURF, color, (left + i, top + BOX_SIZE - 1), (left + BOX_SIZE - 1, top + i))
    elif shape == OVAL:
        # to draw Ellipse give a rectangle points(like x, y, width, height)
        # ellipse left is on left border top below the quarter of the box height
        # long area up to right end of the box and short area is half of the box thickness
        pygame.draw.ellipse(DISPLAY_SURF, color, (left, top + quarter, BOX_SIZE, half))


def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # Draw boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        # Get Left & Top Pixel from Box row & column Number
        left, top = leftTopCoordsOfBox(box[0], box[1])
        # Set the Background Color to the Box area Rectangle(Square actually)
        pygame.draw.rect(DISPLAY_SURF, BG_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
        # Get the Icon of the current box (Tuple of Shape name and color tuple)
        shape, color = getShapeAndColor(board, box[0], box[1])
        # Draw Icon using Shape, Color, coordinates of box
        drawIcon(shape, color, box[0], box[1])
        # This gives the Sliding effect
        if coverage > 0:  # only draw the cover if there is a coverage
            # By Changing Coverage in the tuple Sliding direction will change
            # Right to Left
            pygame.draw.rect(DISPLAY_SURF, BOX_COLOR, (left, top, coverage, BOX_SIZE))
            # Bottom to Top
            # pygame.draw.rect(DISPLAY_SURF, BOX_COLOR, (left, top, BOX_SIZE, coverage))
    pygame.display.update()
    CLOCK.tick(FPS)


# Do the "box reveal" animation.
def revealBoxesAnimation(board, boxesToReveal):
    # For loop for Sliding motion Preview
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, -REVEAL_SPEED):
        # Cover Sliding effect Opening (Coverage from full to -ve)
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        # Cover Sliding effect Closing (Coverage from 0 to full)
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    # Draws all the boxes in their covered or revealed state.
    for boxx in range(BOARD_WIDTH):
        for boxy in range(BOARD_HEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAY_SURF, BOX_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    # Get the left, Top Coordinates
    left, top = leftTopCoordsOfBox(boxx, boxy)
    # Draw a blue(HIGHLIGHT_COLOR) Square around the box(in 4 pixel thick & 1 pixel gap between selection box and box)
    pygame.draw.rect(DISPLAY_SURF, HIGHLIGHT_COLOR, (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE + 10), 4)


# Before Starting Game Show All boxes But not showing all boxes simultaneously
# But in random set of 8
def startGameAnimation(board):
    # Set all Box Revealed Status as False
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    # Generate All Box Index as a list of Tuples(x, y Coordinates)
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            boxes.append((x, y))
    # Shuffle the coordinates List
    random.shuffle(boxes)
    # Get a List of list in every inner list contains 8 boxes coordinates
    # [[(7, 2), (8, 2), (1, 1), (2, 4), (8, 4), (6, 4), (2, 3), (3, 6)],....]
    boxGroups = splitIntoGroupsOf(8, boxes)
    # Draw Boxes
    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        # Reveal The Boxes mentioned in List
        revealBoxesAnimation(board, boxGroup)
        # Cover The Boxes mentioned in List
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHT_BG_COLOR
    color2 = BG_COLOR
    # Background Color Light and Dark Animation
    for i in range(13):
        color1, color2 = color2, color1  # swap colors
        DISPLAY_SURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for column in revealedBoxes:
        if False in column:
            return False  # return False if any boxes are covered.
    return True


# Only Start The Game if the file Accessed Directly
if __name__ == '__main__':
    main()
