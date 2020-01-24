from random import seed, gauss
from datetime import datetime
from time import sleep
from components.mouse import Mouse
from data.constants import *

class MouseController:
    def __init__(self, gameStateManager):
        self.mouse = Mouse()
        self.gameStateManager = gameStateManager
        seed(datetime.now())

    def clickAndWaitUntilStateChange(self, position, std, fromStates, toStates, clickWhileWaiting):
        self.normalSleep()
        while True:
            self.mouse.simulateClick(position, std)
            self.longSleep()
            currentState = self.gameStateManager.updateScreenshotAndState()
            if currentState not in fromStates:
                break
        while currentState not in toStates:
            if clickWhileWaiting:
                for _ in range(NUM_CLICKS_BEFORE_UPDATE):
                    self.mouse.simulateClick(WAITING_CLICK_POSITION, WAITING_CLICK_STD)
                    self.shortSleep()
            else:
                self.normalSleep()
            currentState = self.gameStateManager.updateScreenshotAndState()

    def clickAndNoStageChange(self, position, std):
        self.mouse.simulateClick(position, std)
        self.normalSleep()

    def longSleep(self):
        sleepTime = LONG_CLICK_INTERVAL + gauss(0, LONG_CLICK_INTERVAL_STD)
        sleep(sleepTime)

    def normalSleep(self):
        sleepTime = NORMAL_CLICK_INTERVAL + gauss(0, NORMAL_CLICK_INTERVAL_STD)
        sleep(sleepTime)

    def shortSleep(self):
        sleepTime = SHORT_CLICK_INTERVAL + gauss(0, SHORT_CLICK_INTERVAL_STD)
        sleep(sleepTime)