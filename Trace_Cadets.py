from image import *

refreshRate = 1

gridTextures = []
grids = ( 
    (
        ( (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (0, 2), (0, 1), (1, 1), (1, 0) ),
        ( (0, 0), (2, 0), (2, 1), (0, 1), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (3, 0), (3, 1), (0, 1), (0, 0) ),
        ( (0, 0), (2, 0), (2, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (2, 1), (2, 0), (3, 0), (3, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (0, 1), (0, 0) ),
        ( (1, 0), (1, 1), (0, 1), (1, 0) ),
        ( (0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (1, 1), (1, 0), (0, 0) )
    ),
    (
        ( (1, 0), (2, 0), (2, 2), (0, 2), (0, 1), (1, 1), (1, 0) ),
        ( (0, 0), (1, 0), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (2, 0), (2, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (3, 0), (3, 1), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (2, 0), (2, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (0, 1), (0, 0) ),
        ( (1, 0), (1, 1), (0, 1), (1, 0) )
    ),
    (
        ( (0, 0), (3, 0), (3, 2), (2, 2), (2, 1), (1, 1), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (2, 0), (0, 1), (0, 0) ),
        ( (2, 0), (2, 1), (0, 1), (2, 0) ),
        ( (0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ), 
        ( (0, 0), (2, 0), (2, 1), (0, 1), (0, 0) ),
        ( (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (0, 2), (0, 1), (1, 1), (1, 0) ),
        ( (0, 0), (2, 0), (2, 1), (0, 1), (0, 0) )
    ),
    (
        ( (0, 0), (2, 0), (2, 1), (0, 1), (0, 0) ),
        ( (0, 0), (2, 0), (2, 1), (0, 1), (0, 0) ),
        ( (0, 0), (1, 0), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (2, 0), (2, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (0, 0), (1, 0), (1, 2), (0, 2), (0, 0) ),
        ( (0, 0), (1, 0), (0, 2), (0, 0) ),
        ( (1, 0), (1, 2), (0, 2), (1, 0) ),
        ( (0, 0), (1, 0), (1, 1), (0, 1), (0, 0) ),
        ( (1, 0), (2, 0), (2, 2), (0, 2), (0, 1), (1, 1), (1, 0) ),
        ( (0, 0), (2, 0), (2, 1), (0, 1), (0, 0) ),
        ( (1, 0), (2, 0), (2, 2), (0, 2), (0, 1), (1, 1), (1, 0) )
    )
)

def moveToGridPoint(gridPoint: tuple):
    # The offset from the top-left corner of the screen to the start of grid. 
    gridOffset = ( 55, 55 )
    # Distance from one point on the grid to another. 
    gridSquareSize = 48
    getPointPosition = lambda point: localToGlobalPosition(
        ( gridOffset[0] + point[0] * gridSquareSize,
        gridOffset[1] + point[1] * gridSquareSize ), mainScreen=False
    ) 

    pointPosition = getPointPosition(gridPoint)
    pyautogui.moveTo(pointPosition[0], pointPosition[1], duration=0.2)
def drawShape(shape: tuple):
    firstPoint = True

    # Trace each point in shape. 
    for point in shape:
        moveToGridPoint(point)

        if firstPoint:
            pyautogui.mouseDown()
            firstPoint = False

    pyautogui.mouseUp()

def setup():
    for gridIndex in range(1, len(grids) + 1):
        gridTexture = Image.open(
            f"assets/Trace Cadets/Grid{gridIndex}.png"
        )
        gridTextures.append(gridTexture)
def update():
    mainScreen = takeScreenshot() 
    gridIndex = -1

    # Attempts to locate which grid is being displayed.
    for textureIndex, gridTexture in enumerate(gridTextures):
        if pyautogui.locate(gridTexture, mainScreen, confidence=0.8) is not None:
            gridIndex = textureIndex
            break 
    
    # If no grid is located, then leave the function to restart the search. 
    if gridIndex == -1:
        return

    pyautogui.sleep(2.0)
    # Resets the shape detection system in the minigame. 
    drawShape(( (1, 0), (0, 0) ))

    # Draw each shape in grid. 
    for shape in grids[gridIndex]:
        drawShape(shape)
        pyautogui.sleep(0.8)

    # Exits program once the grid has been fully drawn. 
    exit()