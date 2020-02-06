from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Attendence(State):
	signature = {
		(309, 384) : ((143, 143, 143, 255),),
		(2242, 403) : ((36, 50, 65, 255),),
		(1164, 942) : ((31, 37, 41, 255),),
		(1307, 940) : ((30, 38, 43, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.attendence
		self.transition.update({
			Transitions.confirm : ({StateKey.obtainLoginResource,}, (1280, 929, 6)),
		})
