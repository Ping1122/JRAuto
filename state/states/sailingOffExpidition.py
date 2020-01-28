from state.stateKey import StateKey
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExpidition(SailingOff):
	signature = {
		**SailingOff.signature,
		(1120, 51) : (16, 132, 228, 255),
		(1136, 57) : (172, 213, 245, 255),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.sailingOffExpidition
		self.transition.pop(Transitions.selectExpidition, None)
		self.transition.update({
		})