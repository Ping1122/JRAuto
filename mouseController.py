from time import sleep
from mouse import Mouse
from config import *

class MouseController:
    def __init__(gameStateManager):
        this.mouse = Mouse()
        this.gameStateManager = gameStateManager

    def clickAndWaitUntilStateChange(position, std, fromStates, toStates, clickWhileWaiting):
        while True:
            this.mouse.simulateClick(position, std)
            sleep(2)
            currentState = this.gameStateManager.updateScreenshotAndState()
            if currentState not in fromStates:
                break
        while currentState not in toStates:
            if clickWhilewaiting:
                for (_ in range(5)):
                    this.mouse.simulateClick(WAITING_CLICK_POSITION, WAITING_CLICK_STD)
                    shortSleep()
            else:
                sleep(1)
            currentState = this.gameStateManager.updateScreenshotAndState()

    def clickAndNoStageChange(position, std):
        this.mouse.simulateClick(position, std)
        normalSleep()

    def normalSleep():
        sleepTime = NORMAL_CLICK_INTERVAL + random.gauss(0,NORMAL_CLICK_INTERVAL_STD)
        sleep(sleepTime)

    def shortSleep():
        sleepTime = SHORT_CLICK_INTERVAL + random.gauss(0, SHORT_CLICK_INTERVAL_STD)
        sleep(sleepTime)
