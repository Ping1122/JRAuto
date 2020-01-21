from pynput.mouse import Button, Controller
import random
from datetime import datetime
import time
from monitor import *
from states import *

mouse = Controller()
random.seed(datetime.now())

def singleClick(position, std):
	position = pixelPositionToMousePosition(position)
	std = pixelStdToMouseStd(std)
	moveAndClick(position, std)
	sleepAfterClick()
	img = takeScreenshot()
	state = analyzeState()
	return (img, state)

def clickUntilChangeState(state):
	pass

def pixelPositionToMousePosition(position):
	x = SIMULATOR_WINDOW_POSITION_MOUSE[0] + IMG_RESOLUTION_MOUSE[0]*(position[0]/IMG_RESOLUTION[0])
	y = SIMULATOR_WINDOW_POSITION_MOUSE[1] + IMG_RESOLUTION_MOUSE[1]*(position[1]/IMG_RESOLUTION[1])
	return (int(x), int(y))

def pixelStdToMouseStd(std):
	return int(std * (IMG_RESOLUTION_MOUSE[0] / IMG_RESOLUTION[0]))

def sleepAfterClick():
	sleepTime = CLICK_INTERVAL + random.gauss(0, CLICK_INTERVAL_STD)
	time.sleep(sleepTime)

def moveAndClick(position, std):
	nosie1 = random.gauss(0, std)
	nosie2 = random.gauss(0, std)
	position = (position[0]+nosie1, position[1]+nosie2)
	mouse.position = position
	time.sleep(0.1)
	mouse.press(Button.left)
	mouse.release(Button.left)