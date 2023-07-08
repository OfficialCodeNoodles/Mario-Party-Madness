import time 

from properties import *
from image import *

minigameScripts = ( "Goomba_Wrangler", "Trace_Cadets", "Domino_Effect" )
minigameNames = ( "Goomba Wrangler", "Trace Cadets", "Domino Effect" )
minigameScriptIndex = 0

def initApplication():
    properties.loadFile()
    # This failsafe isn't neccesary since one is built in already. 
    pyautogui.FAILSAFE = False

if __name__ == "__main__":
    try:
        initApplication()

        # Loads in the minigame scripts
        for script in minigameScripts:
            exec(f"import {script}")
    except Exception as exception:
        print(exception)
        exit()

    buttonSelected = pyautogui.confirm(
        "Select a minigame to have the program play", 
        title="Mario Party Madness", buttons=minigameNames + ( "Cancel", )
    ) 

    if buttonSelected == "Cancel" or buttonSelected is None:
        exit()

    minigameScriptIndex = minigameNames.index(buttonSelected)
    minigameScript = minigameScripts[minigameScriptIndex]
    applicationOpen = True

    eval(f"{minigameScript}.setup()")

    # Amount of time required for each fram (in seconds).
    frameDuration = 1.0 / eval(f"{minigameScript}.refreshRate")

    while applicationOpen:
        startTime = time.time() 

        eval(f"{minigameScript}.update()")

        endTime = time.time()
        difference = endTime - startTime
        time.sleep(max(frameDuration - difference, 0.0))

        # Exits program when mouse is put into the top-left corner. 
        mousex, mousey = pyautogui.position()
        applicationOpen = mousex + mousey != 0 