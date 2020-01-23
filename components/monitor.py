from PIL import Image, ImageGrab
from ..data.constants import SIMULATOR_WINDOW_POSITION

class Monitor:
	def __init__(self):
		pass

	def takeScreenshot(self):
		img = ImageGrab.grab(bbox = SIMULATOR_WINDOW_POSITION)
		return img
