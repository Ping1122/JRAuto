from PIL import Image, ImageGrab
from states import *
from config import *
from util import *
from dangers import *

class Monitor:
	def __init__(self):
		pass

	def takeScreenshot(self):
		img = ImageGrab.grab(bbox = SIMULATOR_WINDOW_POSITION)
		return img
