from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ExerciseOpponentDetail(State):
	signature = {
		(535, 352) : ((104, 149, 192, 255), ),
		(217, 1065) : ((188, 188, 188, 255), ),
		(759, 1040) : ((123, 123, 123, 255), ),
		(2343, 361) : ((224, 224, 224, 255), ),
	}
	def __init__(self):
		super(ExerciseOpponentDetail, self).__init__()
		self.key = StateKey.exerciseOpponentDetail
		self.transition.update({
            Transitions.close : ({StateKey.sailingOffExercise, }, (2347, 359, 6)),
            Transitions.challenge : ({StateKey.combatPreparationStatistic, }, (2171, 1056, 6)),
        })



