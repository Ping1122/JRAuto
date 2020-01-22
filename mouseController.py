from time import sleep
from mouse import Mouse
from config import *
import random

class MouseController:
    def __init__(self, gameStateManager):
        self.mouse = Mouse()
        self.gameStateManager = gameStateManager

    def clickAndWaitUntilStateChange(self, position, std, fromStates, toStates, clickWhileWaiting):
        sleep(2)
        self.mouse.simulateClick(position, std)
        sleep(2)
        currentState = self.gameStateManager.updateScreenshotAndState()
        while currentState not in toStates:
            if clickWhileWaiting:
                for _ in range(5):
                    self.mouse.simulateClick(WAITING_CLICK_POSITION, WAITING_CLICK_STD)
                    self.shortSleep()
            else:
                sleep(1)
            currentState = self.gameStateManager.updateScreenshotAndState()

    def clickAndNoStageChange(self, position, std):
        self.mouse.simulateClick(position, std)
        self.normalSleep()

    def normalSleep(self):
        sleepTime = NORMAL_CLICK_INTERVAL + random.gauss(0,NORMAL_CLICK_INTERVAL_STD)
        sleep(sleepTime)

    def shortSleep(self):
        sleepTime = SHORT_CLICK_INTERVAL + random.gauss(0, SHORT_CLICK_INTERVAL_STD)
        sleep(sleepTime)
