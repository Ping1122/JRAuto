from state.stateKey import StateKey
from state.signals import Signals
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExpidition(SailingOff):
	signature = {
		**SailingOff.signature,
		(1120, 51) : ((16, 132, 228, 255),),
		(1136, 57) : ((172, 213, 245, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.sailingOffExpidition
		self.transition.pop(Transitions.selectExpidition, None)
		self.transition.update({
			Transitions.collectExpidition1 : ((StateKey.continueExpidition,), (2311, 393, 8), True),
			Transitions.collectExpidition2 : ((StateKey.continueExpidition,), (2311, 676, 8), True),
			Transitions.collectExpidition3 : ((StateKey.continueExpidition,), (2311, 964, 8), True),
			Transitions.collectExpidition4 : ((StateKey.continueExpidition,), (2311, 1249, 8), True),
		})
		self.sign.update({
			Signals.expidition1Completed : {
				(2335, 398) : ((0, 0, 0, 255),),
			},
			Signals.expidition2Completed : {
				(2298, 661) : ((0, 0, 0, 255),),
			},
			Signals.expidition3Completed : {
				(2250, 952) : ((0, 0, 0, 255),),
			},
			Signals.expidition4Completed : {
				(2255, 1258) : ((0, 0, 0, 255),),
			},
		})