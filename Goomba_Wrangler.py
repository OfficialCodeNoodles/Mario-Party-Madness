from enum import Enum
import math

from image import * 

refreshRate = 10

class Entities(Enum):
    Goomba = 0 
    Bomb = 1

entityTextures = []

def circleArea(origin: tuple, radius: float, mainScreen=True):
    points = 12
    arcLength = 360 // points
    borderThickness = ( 18, 12 )
    firstPoint = True

    for angle in range(0, 360 + arcLength * 2, arcLength):
        radians = angle / (180.0 / math.pi)
        offset = ( radius * math.cos(radians), radius * math.sin(radians) )
        # Calculate position by adding the offset to the origin of the circle. 
        position = [ origin[0] + offset[0], origin[1] + offset[1] ]
        # Constrain the position to the games borders. 
        position[0] = min(max(position[0], borderThickness[0]), 
            dsWidth - borderThickness[0])
        position[1] = min(max(position[1], borderThickness[1]), 
            dsHeight - borderThickness[1])
        # Transform the position to global screen space. 
        position = localToGlobalPosition(position, mainScreen)
            
        pyautogui.moveTo(position[0], position[1])

        if firstPoint:
            pyautogui.mouseDown()
            firstPoint = False
        
    pyautogui.sleep(0.03)
    pyautogui.mouseUp()
def distance(point1: tuple, point2: tuple) -> float:
    return math.sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))

def setup():
    pyautogui.MINIMUM_DURATION = 0.03
    pyautogui.PAUSE = 0.02

    for entity in Entities:
        for textureIndex in range(1, 3):
            entityTexture = Image.open(
                f"assets/Goomba Wrangler/{entity.name}{textureIndex}.png"
            )
            entityTextures.append(entityTexture)
def update():
    subScreen = takeScreenshot(mainScreen=False)

    goombas = []
    bombs = []
    entityConfidence = 0.65

    # Locates all goombas and bombs on screen, and adds them to their 
    # coresponding lists. 
    for textureIndex in range(2):
        goombas += pyautogui.locateAll(
            entityTextures[Entities.Goomba.value + textureIndex], subScreen, 
            confidence=entityConfidence
        )
        bombs += pyautogui.locateAll(
            entityTextures[Entities.Bomb.value + textureIndex + 1], subScreen, 
            confidence=entityConfidence
        )

    goombaBombsDistances = []

    for goomba in goombas:
        goombaCenter = pyautogui.center(goomba)
        minDistance = dsWidth
        
        for bomb in bombs:
            bombCenter = pyautogui.center(bomb)
            goombaBombsDistance = distance(goombaCenter, bombCenter)
            minDistance = min(minDistance, goombaBombsDistance)
        
        goombaBombsDistances.append(minDistance)

    goombaIndex = -1
    goombaMaxDistance = 0.0

    # Locates the goomba that is the farthest distance from any bombs. 
    for index, goombaBombsDistance in enumerate(goombaBombsDistances):
        if goombaBombsDistance > goombaMaxDistance:
            goombaMaxDistance = goombaBombsDistance
            goombaIndex = index
    
    if goombaIndex != -1:
        goombaBombsDistance = goombaBombsDistances[goombaIndex]

        # Ensures the distance between the goomba and the bomb isn't too small.
        if goombaBombsDistance > 25.0 * math.sqrt(2):
            goombaCenter = pyautogui.center(goombas[goombaIndex])
            # Calculates a circle radius based on how close the nearest bomb 
            # is. Note: The farther the bomb, the bigger the circle. 
            circleRadius = max(15.0, min(25.0, goombaBombsDistance / 2))

            circleArea(goombaCenter, circleRadius, mainScreen=False)