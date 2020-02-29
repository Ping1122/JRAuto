from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ChaseOrGiveUp(State):
	signature = {
		(208, 242) : ( (214, 211, 214), ),
		(260, 269) : ( (255, 243, 132), ),
		(264, 295) : ( (156, 190, 107), ),
		(266, 332) : ( (156, 4, 8), ),
	}
	def __init__(self):
		super(ChaseOrGiveUp, self).__init__()
		self.key = StateKey.chaseOrGiveUp
		resultStates = {
			StateKey.battleResult,
		}
		self.transition.update({
			Transitions.chase : (resultStates, (242, 334, 2)),
			Transitions.giveUp : (resultStates, (459, 335, 2)),
		})
