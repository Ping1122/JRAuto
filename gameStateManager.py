from monitor import Monitor
from logger import *

class GameStateManager:
    def __init__:
        this.monitor = Monitor()
        updateScreenshotAndState()

    def updateScreenshotAndState():
    	this.currentScreenshot = this.monitor.takeScreenshot()
    	this.currentState = this.analyzeState()
        return this.currentState

    def analyzeState():
    	imgData = this.currentScreenshot.getdata()
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

    def findDamagedShips():
    	imgData = currentScreenshot.getdata()
    	damagedShips = []
    	for ship, signature in normalSignature.items():
    		if all(
    			imgData[pixelPostionToImageDataIndex(pos)] != color
    			for pos, color in signature.items()
    		):
    			damagedShips.append(ship)
    	return damagedShips

    def checkStage74bExistsSubmarine():
    	imgData = currentScreenshot.getdata()
    	return all(
    		imgData[pixelPostionToImageDataIndex(pos)] == color
    		for pos, color in stage74bExistsSubmarineSignature.items()
    	)

    def assertCurrentStates(states, description):
    	if currentState not in state:
    		message = "Trying to " + description + ", but not in "+ str(states) + " screen."
    		log(message, Types.error)
    		exit(1)
