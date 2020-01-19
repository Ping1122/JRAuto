from PIL import Image, ImageGrab
from states import States
from config import *

def analyzeScreenShotForState(img):
	return States.unknown

def takeScreenShot():
	img = ImageGrab.grab(bbox = SIMULATOR_WINDOW_POSITION)
	return img