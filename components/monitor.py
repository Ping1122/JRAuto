from threading import Lock
from PIL import Image, ImageGrab
from components.window import Window

class Monitor:
	lock = Lock()

	def __init__(self):
		self.window = Window()

	def takeScreenshot(self):
		with self.lock:
			img = ImageGrab.grab(bbox = self.window.getWindow())
			return img
