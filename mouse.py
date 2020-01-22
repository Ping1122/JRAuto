from pynput.mouse import Button, Controller
import random
from datetime import datetime
import time
from config import *

class Mouse:
	def __init__(self):
		self.mouse = Controller()
		random.seed(datetime.now())

	def simulateClick(self, position, std):
		position = self.pixelPositionToMousePosition(position)
		std = self.pixelStdToMouseStd(std)
		self.moveAndClick(position, std)

	def pixelPositionToMousePosition(self, position):
		x = SIMULATOR_WINDOW_POSITION_MOUSE[0] + IMG_RESOLUTION_MOUSE[0]*(position[0]/IMG_RESOLUTION[0])
		y = SIMULATOR_WINDOW_POSITION_MOUSE[1] + IMG_RESOLUTION_MOUSE[1]*(position[1]/IMG_RESOLUTION[1])
		return (int(x), int(y))

	def pixelStdToMouseStd(self, std):
		return int(std * (IMG_RESOLUTION_MOUSE[0] / IMG_RESOLUTION[0]))

	def moveAndClick(self, position, std):
		nosie1 = random.gauss(0, std)
		nosie2 = random.gauss(0, std)
		position = (position[0]+nosie1, position[1]+nosie2)
		self.mouse.position = position
		time.sleep(0.1)
		self.mouse.press(Button.left)
		self.mouse.release(Button.left)
