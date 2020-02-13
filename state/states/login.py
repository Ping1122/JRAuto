from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Login(State):
	signature = {
		(72, 1192) : ((183, 197, 201, 255), ),
		(206, 1170) : ((237, 237, 237, 255), ),
		(114, 1309) : ((255, 255, 255, 255), ),
		(2167, 1220) : ((53, 53, 53, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.login
		self.transition.update({
			Transitions.login : ({
				StateKey.home,
			}, (2270, 1234, 10))
		})
