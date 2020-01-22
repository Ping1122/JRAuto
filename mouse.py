from pynput.mouse import Button, Controller
import random
from datetime import datetime
import time

class Mouse:
	def __init__():
		this.mouse = Controller()
		random.seed(datetime.now())

	def simulateClick(position, std):
		position = this.pixelPositionToMousePosition(position)
		std = this.pixelStdToMouseStd(std)
		this.moveAndClick(position, std)

	def pixelPositionToMousePosition(position):
		x = SIMULATOR_WINDOW_POSITION_MOUSE[0] + IMG_RESOLUTION_MOUSE[0]*(position[0]/IMG_RESOLUTION[0])
		y = SIMULATOR_WINDOW_POSITION_MOUSE[1] + IMG_RESOLUTION_MOUSE[1]*(position[1]/IMG_RESOLUTION[1])
		return (int(x), int(y))

	def pixelStdToMouseStd(std):
		return int(std * (IMG_RESOLUTION_MOUSE[0] / IMG_RESOLUTION[0]))

	def moveAndClick(position, std):
		nosie1 = random.gauss(0, std)
		nosie2 = random.gauss(0, std)
		position = (position[0]+nosie1, position[1]+nosie2)
		this.mouse.position = position
		time.sleep(0.1)
		this.mouse.press(Button.left)
		this.mouse.release(Button.left)
