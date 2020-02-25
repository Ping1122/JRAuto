from copy import copy
from state.stateKey import StateKey
from state.signals import Signals
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExercise(SailingOff):
	signature = copy(SailingOff.signature)
	signature.update({
		(795, 59) : ((16, 132, 228, 255),),
		(853, 41) : ((247, 251, 254, 255),),
		(2473, 804) : ((179, 186, 194, 255), ),
		(2471, 881) : ((181, 189, 196, 255), ),
		(1368, 682) : ((237, 237, 237, 255), ),
		(1186, 721) : ((237, 237, 237, 255), (37, 71, 105, 255)),
		(1202, 765) : ((25, 60, 93, 255), (237, 237, 237, 255)),
	})
	def __init__(self):
		super(SailingOffExercise, self).__init__()
		self.key = StateKey.sailingOffExercise
		self.sign.update({
			Signals.noMoreExerciseTrials : {
				(2104, 308) : ((206, 226, 236, 255), ),
				(2104, 604) : ((206, 226, 236, 255), ),
				(2104, 900) : ((206, 226, 236, 255), ),
				(2104, 1195) : ((227, 233, 237, 255), ),
			},
			Signals.opponent1Available : {
				(1986, 377) : ((25, 128, 223, 255), ),
			},
			Signals.opponent2Available : {
				(1992, 672) : ((25, 128, 224, 255), ),
			},
			Signals.opponent3Available : {
				(1995, 963) : ((26, 129, 226, 255), ),
			},
			Signals.opponent4Available : {
				(1995, 1261) : ((26, 129, 225, 255), ),
			},
			Signals.opponent5Available : {
				(1992, 1198) : ((27, 129, 226, 255), ),
			},
		})
		self.transition.pop(Transitions.selectExercise, None)
		self.transition.update({
			Transitions.selectopponent1 : ({StateKey.exerciseOpponentDetail, }, (714, 318, 10)),
			Transitions.selectopponent2 : ({StateKey.exerciseOpponentDetail, }, (713, 616, 10)),
			Transitions.selectopponent3 : ({StateKey.exerciseOpponentDetail, }, (713, 918, 10)),
			Transitions.selectopponent4 : ({StateKey.exerciseOpponentDetail, }, (714, 1216, 10)),
			Transitions.selectopponent5 : ({StateKey.exerciseOpponentDetail, }, (714, 1157, 10)),
		})
		self.behavior.update({
			Behaviors.scrollUp : ((2428, 1248, 5), (2426, 406, 5))
		})
