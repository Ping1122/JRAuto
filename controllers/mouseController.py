from random import seed, gauss
from datetime import datetime
from time import sleep
from components.mouse import Mouse
from data.constants import *

class MouseController:
    def __init__(self, stateController):
        self.mouse = Mouse()
        self.stateController = stateController
        seed(datetime.now())

    def clickAndWaitUntilStateChange(self, clickInfo, fromState, toStates, clickWhileWaiting):
        self.normalSleep()
        while True:
            self.mouse.simulateClick(clickInfo)
            self.longSleep()
            currentState = self.stateController.updateState()
            if currentState != fromState:
                break
        print(toStates)
        while currentState not in toStates:
            if clickWhileWaiting:
                for _ in range(NUM_CLICKS_BEFORE_UPDATE):
                    self.mouse.simulateClick(WAITING_CLICK_INFO)
                    self.shortSleep()
            else:
                self.normalSleep()
            currentState = self.stateController.updateState()

    def clickAndNoStageChange(self, clickInfo):
        self.mouse.simulateClick(clickInfo)
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
