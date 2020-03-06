from state.state import State
from state.stateKey import StateKey

class Unknown(State):
	def __init__(self):
		super(Unknown, self).__init__()
		self.key = StateKey.unknown