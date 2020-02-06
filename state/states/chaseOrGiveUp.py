from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ChaseOrGiveUp(State):
	signature = {
		(766, 601) : ((176, 176, 176, 255),),
		(953, 702) : ((185, 194, 111, 255),),
		(842, 921) : ((228, 187, 187, 255),),
		(1644, 917) : ((121, 189, 253, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.chaseOrGiveUp
		resultStates = {
			StateKey.battleResult,
		}
		self.transition.update({
			Transitions.chase : (resultStates, (885, 938, 7)),
			Transitions.giveUp : (resultStates, (1677, 938, 7)),
		})
