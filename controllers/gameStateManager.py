from util.util import pixelPostionToImageDataIndex
from util.messages import Messages
from util.logger import log, Types
from data.states import States, stateSignature
from data.dangers import *
from components.monitor import Monitor

class GameStateManager:
    def __init__(self):
        self.messages = Messages()
        self.monitor = Monitor()
        self.updateScreenshotAndState()

    def updateScreenshotAndState(self):
        self.currentScreenshot = self.monitor.takeScreenshot()
        self.currentState = self.analyzeState()
        log(str(self.currentState), Types.debug)
        return self.currentState

    def analyzeState(self):
        imgData = self.currentScreenshot.getdata()
        for state, signature in stateSignature.items():
            if all(
                #debug(state, imgData, pos, color)
                imgData[pixelPostionToImageDataIndex(pos)] == color
                for pos, color in signature.items()
            ):
                return state
        return States.unknown

    def debug(state, imgData, pos, color):
        if state == States.enemyInfo:
            print(imgData[pixelPostionToImageDataIndex(pos)], color)
        return imgData[pixelPostionToImageDataIndex(pos)] == color

    def findDamagedShips(self):
        imgData = self.currentScreenshot.getdata()
        damagedShips = []
        for ship, signature in normalSignature.items():
            if all(
                imgData[pixelPostionToImageDataIndex(pos)] != color
                for pos, color in signature.items()
            ):
                damagedShips.append(ship)
        return damagedShips

    def checkStage74bExistsSubmarine(self):
        imgData = self.currentScreenshot.getdata()
        return all(
            imgData[pixelPostionToImageDataIndex(pos)] == color
            for pos, color in stage74bExistsSubmarineSignature.items()
        )

    def assertCurrentStates(self, states, description):
        if self.currentState not in states:
            message = self.messages.assertStateFailMessage(description)
            log(message, Types.error)
            exit(1)
