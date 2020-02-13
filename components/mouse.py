from pynput.mouse import Button, Controller
from random import seed, gauss
from datetime import datetime
from time import sleep
from data.constants import *

class Mouse:
	def __init__(self):
		self.mouse = Controller()
		seed(datetime.now())

	def simulateClick(self, clickInfo):
		clickInfo = self.pixelToMouse(clickInfo)
		self.moveAndClick(clickInfo)

	def simulateScroll(self, scrollInfo):
		scrollInfo = (
			self.pixelToMouse(scrollInfo[0]),
			self.pixelToMouse(scrollInfo[1]),
		)
		self.moveAndScroll(scrollInfo)

	def pixelToMouse(self, clickInfo):
		x = SIMULATOR_WINDOW_POSITION_MOUSE[0] + IMG_RESOLUTION_MOUSE[0]*(clickInfo[0]/IMG_RESOLUTION[0])
		y = SIMULATOR_WINDOW_POSITION_MOUSE[1] + IMG_RESOLUTION_MOUSE[1]*(clickInfo[1]/IMG_RESOLUTION[1])
		z = clickInfo[2] * (IMG_RESOLUTION_MOUSE[0] / IMG_RESOLUTION[0])
		return (int(x), int(y), int(z))

	def moveAndClick(self, clickInfo):
		position = self.generateClickPosition(clickInfo)
		self.mouse.position = position
		sleep(MOVE_CLICK_INTERVAL)
		self.mouse.press(Button.left)
		self.mouse.release(Button.left)

	def moveAndScroll(self, scrollInfo):
		startPosition = self.generateClickPosition(scrollInfo[0])
		endPosition = self.generateClickPosition(scrollInfo[1])
		deltaX = endPosition[0] - startPosition[0]
		deltaY = endPosition[1] - startPosition[1]
		self.mouse.position = startPosition
		sleep(MOVE_CLICK_INTERVAL)
		self.mouse.press(Button.left)
		self.mouse.move(deltaX, deltaY)
		self.mouse.release(Button.right)

	def generateClickPosition(self, clickInfo):
		nosie1 = gauss(0, clickInfo[2])
		nosie2 = gauss(0, clickInfo[2])
		position = (clickInfo[0]+nosie1, clickInfo[1]+nosie2)
		return position
