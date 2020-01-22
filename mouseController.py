from time import sleep
from mouse import *
from config import *

class MouseController:
    def __init__(gameStateManager):
        this.gameStateManager = gameStateManager

    def clickAndWaitUntilStateChange(position, std, fromStates, toStates, clickWhileWaiting):
        (position, std) = pixelToMouseResolution(position, std)
        while True:
            simulateClick(position, std)
            sleep(2)
            currentState = this.gameStateManager.updateScreenshotAndState()
            if currentState not in fromStates:
                break
        while currentState not in toStates:
            if clickWhilewaiting:
                for (_ in range(5)):
                    simulateClick(WAITING_CLICK_POSITION, WAITING_CLICK_STD)
                    shortSleep()
            else:
                sleep(1)
            currentState = this.gameStateManager.updateScreenshotAndState()

    def clickAndNoStageChange(position, std):
        (position, std) = pixelToMouseResolution(position, std)
        simulateClick(position, std)
        normalSleep()

    def pixelToMouseResolution(position, std):
        x = SIMULATOR_WINDOW_POSITION_MOUSE[0] + IMG_RESOLUTION_MOUSE[0]*(position[0]/IMG_RESOLUTION[0])
    	y = SIMULATOR_WINDOW_POSITION_MOUSE[1] + IMG_RESOLUTION_MOUSE[1]*(position[1]/IMG_RESOLUTION[1])
    	std = int(std * (IMG_RESOLUTION_MOUSE[0] / IMG_RESOLUTION[0]))
        return ((x, y), std)

    def normalSleep():
    	sleepTime = NORMAL_CLICK_INTERVAL + random.gauss(0,NORMAL_CLICK_INTERVAL_STD)
    	sleep(sleepTime)

    def shortSleep():
    	sleepTime = SHORT_CLICK_INTERVAL + random.gauss(0, SHORT_CLICK_INTERVAL_STD)
    	sleep(sleepTime)
