from state.stateKey import StateKey
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExercise(SailingOff):
	signature = {
		**SailingOff.signature,
		(795, 59) : (16, 132, 228, 255),
		(853, 41) : (247, 251, 254, 255),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.sailingOffExercise
		self.transition.pop(Transitions.selectExercise, None)
		self.transition.update({
		})
		