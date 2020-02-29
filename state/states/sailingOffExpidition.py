from copy import copy
from state.stateKey import StateKey
from state.signals import Signals
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExpidition(SailingOff):
	signature = copy(SailingOff.signature)
	signature.update({
		(289, 56) : ((16, 134, 231), ),
		(300, 48) : ((255, 255, 255), ),
	})
	def __init__(self):
		super(SailingOffExpidition, self).__init__()
		self.key = StateKey.sailingOffExpidition
		self.transition.pop(Transitions.selectExpidition, None)
		self.transition.update({
			Transitions.collectExpidition1 : ({
					StateKey.expiditionResult, 
					StateKey.continueExpidition
				}, (632, 186, 2)),
			Transitions.collectExpidition2 : ({
					StateKey.expiditionResult, 
					StateKey.continueExpidition
				}, (632, 266, 2)),
			Transitions.collectExpidition3 : ({
					StateKey.expiditionResult, 
					StateKey.continueExpidition
				}, (632, 344, 2)),
			Transitions.collectExpidition4 : ({
					StateKey.expiditionResult, 
					StateKey.continueExpidition
				}, (632, 422, 2)),
			})
		self.sign.update({
			Signals.expidition1Completed : {
				(635, 184) : ((16, 12, 0), ),
			},
			Signals.expidition2Completed : {
				(635, 262) : ((24, 24, 8), ),
			},
			Signals.expidition3Completed : {
				(2250, 952) : ((0, 0, 0, 255),),
			},
			Signals.expidition4Completed : {
				(2255, 1258) : ((0, 0, 0, 255),),
			},
		})
