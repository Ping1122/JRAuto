from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ExerciseOpponentDetail(State):
	signature = {
		(143, 168) : ((66, 125, 181), ),
		(580, 361) : ((82, 170, 247), ),
		(599, 369) : ((173, 211, 247), ),
		(590, 361) : ((74, 166, 247), ),
	}
	def __init__(self):
		super(ExerciseOpponentDetail, self).__init__()
		self.key = StateKey.exerciseOpponentDetail
		self.transition.update({
            Transitions.close : ({StateKey.sailingOffExercise, }, (647, 176, 1)),
            Transitions.challenge : (
            	{StateKey.combatPreparationStatistic, }, 
            	(594, 368, 2)
            ),
        })



