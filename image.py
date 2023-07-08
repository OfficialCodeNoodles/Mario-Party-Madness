import pyautogui
from PIL import Image
import cv2

from properties import *

dsWidth = 256
dsHeight = 192

def takeScreenshot(mainScreen: bool=True) -> Image:
    # Takes a screenshot based on which screen is required. 
    screenshot = pyautogui.screenshot(
        region=properties.mainScreenRegion if mainScreen
            else properties.subScreenRegion
    )
    screenshotSize = screenshot.size
    # Resizes image to match the size of the originial DS screen. 
    scale = properties.mainScreenScale if mainScreen\
        else properties.subScreenScale
    return screenshot.resize(
        ( int(screenshotSize[0] / scale), int(screenshotSize[1] / scale ) ), 
        Image.NEAREST
    )
def localToGlobalPosition(position: tuple, mainScreen: bool=True) -> list:
    scale = properties.mainScreenScale if mainScreen\
        else properties.subScreenScale
    offset = properties.mainScreenRegion if mainScreen\
        else properties.subScreenRegion
    return [
        position[0] * scale + offset[0], 
        position[1] * scale + offset[1]
    ]