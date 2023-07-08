import pydirectinput

from image import *

refreshRate = 5

buttonTextures = []
buttons = ( 'd', 's', 'w', 'a' ) # Corresponds to A, B, X, Y

def setup():
    pydirectinput.FAILSAFE = False

    for buttonIndex in range(1, len(buttons) + 1):
        buttonTexture = Image.open(
            f"assets/Domino Effect/Button{buttonIndex}.png"
        )
        buttonTextures.append(buttonTexture)
def update():
    subScreen = takeScreenshot(mainScreen=False)
    leftMostSide = 160

    for buttonIndex, buttonTexture in enumerate(buttonTextures):
        buttonLocation = pyautogui.locate(
            buttonTexture, subScreen, confidence=0.6
        )

        if buttonLocation is not None:
            # If the button's left side is far left enough, it is pressed.  
            if buttonLocation.left < leftMostSide:
                pydirectinput.press(buttons[buttonIndex])
                return