from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ObtainLoginResource(State):
	signature = {
		(773, 481) : ((237, 237, 237, 255),),
		(838, 371) : ((237, 237, 237, 255),),
		(1189, 798) : ((56, 137, 237, 255),),
		(1392, 824) : ((55, 136, 236, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.obtainLoginResource
		self.transition.update({
			Transitions.obtainResource : ((StateKey.home,), (1282, 800, 6), False),
		})
