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

    def clickAndWaitUntilStateChange(self, clickInfo, fromState, toStates):
        self.normalSleep()
        while True:
            self.mouse.simulateClick(clickInfo)
            self.longSleep()
            currentState = self.stateController.handleStateChange()
            if currentState != fromState:
                break
        while currentState not in toStates:
            self.normalSleep()
            currentState = self.stateController.handleStateChange()

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
