from state.stateKey import StateKey
from state.signals import Signals
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffExercise(SailingOff):
	signature = {
		**SailingOff.signature,
		(795, 59) : ((16, 132, 228, 255),),
		(853, 41) : ((247, 251, 254, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.sailingOffExercise
		self.sign.update({
			Signals.noMoreExerciseTrials : {
				(2104, 308) : ( (206, 226, 236, 255), ),
				(2104, 604) : ( (206, 226, 236, 255), ),
				(2104, 900) : ( (206, 226, 236, 255), ),
				(2104, 1195) : ( (227, 233, 237, 255), ),
			},
			Signals.opponent1Available : {},
			Signals.opponent2Available : {},
			Signals.opponent3Available : {},
			Signals.opponent4Available : {},
			Signals.opponent5Available : {},
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
			Behaviors.scrollUp : ()
		})
