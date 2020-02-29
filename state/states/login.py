from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Login(State):
	signature = {
		(592, 392) : ((239, 239, 239), ),
		(565, 453) : ((255, 211, 49), ),
		(674, 459) : ((247, 223, 49), ),
		(43, 458) : ((239, 239, 239), ),
	}
	def __init__(self):
		super(Login, self).__init__()
		self.key = StateKey.login
		self.transition.update({
			Transitions.login : ({
				StateKey.home,
			}, (620, 454, 2))
		})
