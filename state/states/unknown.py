from state.state import State
from state.stateKey import StateKey

class Unknown(State):
	def __init__(self):
		super().__init__()
		self.key = StateKey.unknown