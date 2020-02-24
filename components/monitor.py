from threading import Lock
from PIL import Image, ImageGrab
from data.constants import SIMULATOR_WINDOW_POSITION

class Monitor:
	lock = Lock()

	def __init__(self):
		pass

	def takeScreenshot(self):
		with self.lock:
			img = ImageGrab.grab(bbox = SIMULATOR_WINDOW_POSITION)
			return img
