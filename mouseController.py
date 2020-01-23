from time import sleep
from mouse import Mouse
from config import *
import random

class MouseController:
    def __init__(self, gameStateManager):
        self.mouse = Mouse()
        self.gameStateManager = gameStateManager

    def clickAndWaitUntilStateChange(self, position, std, fromStates, toStates, clickWhileWaiting):
        this.longSleep()
        self.mouse.simulateClick(position, std)
        this.normalSleep()
        currentState = self.gameStateManager.updateScreenshotAndState()
        while currentState not in toStates:
            if clickWhileWaiting:
                for _ in range(NUM_CLICKS_BEFORE_UPDATE):
                    self.mouse.simulateClick(WAITING_CLICK_POSITION, WAITING_CLICK_STD)
                    self.shortSleep()
            else:
                this.normalSleep()
            currentState = self.gameStateManager.updateScreenshotAndState()

    def clickAndNoStageChange(self, position, std):
        self.mouse.simulateClick(position, std)
        self.normalSleep()

    def longSleep(self):
        sleepTime = LONG_CLICK_INTERVAL + random.gauss(0, LONG_CLICK_INTERVAL_STD)
        sleep(sleepTime)

    def normalSleep(self):
        sleepTime = NORMAL_CLICK_INTERVAL + random.gauss(0, NORMAL_CLICK_INTERVAL_STD)
        sleep(sleepTime)

    def shortSleep(self):
        sleepTime = SHORT_CLICK_INTERVAL + random.gauss(0, SHORT_CLICK_INTERVAL_STD)
        sleep(sleepTime)
