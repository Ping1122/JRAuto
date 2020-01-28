from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Home(State):
	signature = {
		(2378, 1344) : (97, 112, 123, 255),
		(2371, 1137) : (72, 72, 72, 255),
		(2016, 1238) : (255, 246, 226, 255),
		(1700, 1290) : (55, 134, 208, 255),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.home
		self.transition.update({
			Transitions.sailingOff : ((StateKey.sailingOffCombat, StateKey.sailingOffExpidition), (2400, 1298, 10), False),
		})