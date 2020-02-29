from copy import copy
from state.stateKey import StateKey
from state.signals import Signals
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExercise(SailingOff):
	signature = copy(SailingOff.signature)
	signature.update({
		(199, 53) : ((16, 134, 231), ),
		(228, 48) : ((255, 255, 255), ),
		(331, 256) : ((239, 239, 239), ),
		(328, 286) : ((239, 239, 239), ),
		(370, 289) : ((239, 239, 239), ),
		(365, 252) : ((24, 56, 90), ),
	})
	def __init__(self):
		super(SailingOffExercise, self).__init__()
		self.key = StateKey.sailingOffExercise
		self.sign.update({
			Signals.opponent1Available : {
				(568, 126) : ((33, 142, 247), ),
			},
			Signals.opponent2Available : {
				(568, 210) : ((33, 138, 239), ),
			},
			Signals.opponent3Available : {
				(568, 289) : ((33, 142, 239), ),
			},
			Signals.opponent4Available : {
				(563, 370) : ((33, 142, 239), ),
			},
			Signals.opponent5Available : {
				(564, 453) : ((33, 138, 239), ),
			},
		})
		self.transition.pop(Transitions.selectExercise, None)
		self.transition.update({
			Transitions.selectopponent1 : (
				{StateKey.exerciseOpponentDetail, }, 
				(589, 127, 2)
			),
			Transitions.selectopponent2 : (
				{StateKey.exerciseOpponentDetail, }, 
				(589, 210, 2)
			),
			Transitions.selectopponent3 : (
				{StateKey.exerciseOpponentDetail, }, 
				(589, 290, 2)
			),
			Transitions.selectopponent4 : (
				{StateKey.exerciseOpponentDetail, }, 
				(589, 371, 2)
			),
			Transitions.selectopponent5 : (
				{StateKey.exerciseOpponentDetail, }, 
				(589, 452, 2)
			),
		})
