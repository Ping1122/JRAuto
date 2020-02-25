from data.constants import IMG_RESOLUTION

class State(object):
	signature = dict()
	def __init__(self):
		self.sign = dict()
		self.transition = dict()
		self.behavior = dict()
		self.signal = dict()

	def __str__(self):
		return str(self.key)[9:]

	def __hash__(self):
		return hash(self.key)