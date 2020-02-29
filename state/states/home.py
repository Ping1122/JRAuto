from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Home(State):
	signature = {
		(483, 466) : ((214, 97, 90), ),
		(547, 485) : ((173, 186, 189), ),
		(561, 470) : ((99, 69, 90), ),
		(615, 437) : ((24, 28, 24), ),
	}
	def __init__(self):
		super(Home, self).__init__()
		self.key = StateKey.home
		self.transition.update({
			Transitions.sailingOff : ({
				StateKey.sailingOffCombat,
				StateKey.sailingOffExpidition
			}, (658, 471, 4)),
		})
