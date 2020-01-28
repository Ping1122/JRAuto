from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Login(State):
	signature = {
		(72, 1192) : (182, 196, 200, 255),
		(206, 1170) : (237, 237, 237, 255),
		(114, 1309) : (255, 255, 255, 255),
		(2167, 1220) : (53, 53, 53, 255),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.login
		self.transition.update({
			Transitions.login : ((StateKey.home, StateKey.newsAndAnnouncement), (2270, 1234, 10), False)
		})