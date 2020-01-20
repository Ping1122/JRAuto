from PIL import Image, ImageGrab
from states import States
from config import *

def analyzeScreenshotForState(img):
	return States.unknown

def takeScreenshot():
	img = ImageGrab.grab(bbox = SIMULATOR_WINDOW_POSITION)
	return img