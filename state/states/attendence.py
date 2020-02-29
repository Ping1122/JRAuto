from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Attendence(State):
	signature = {
		(106, 177) : ((255, 255, 255),),
		(317, 319) : ((255, 215, 43),),
		(377, 327) : ((174, 150, 42),),
		(361, 324) : ((172, 148, 41),),
	}
	def __init__(self):
		super(Attendence, self).__init__()
		self.key = StateKey.attendence
		self.transition.update({
			Transitions.confirm : (
				{StateKey.obtainLoginResource, }, 
				(357, 329, 3)
			),
		})
