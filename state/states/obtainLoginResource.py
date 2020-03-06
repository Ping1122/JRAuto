from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ObtainLoginResource(State):
	signature = {
		(222, 173) : ((255, 255, 255), ),
		(225, 179) : ((57, 134, 189), ),
		(236, 179) : ((82, 146, 198), ),
		(333, 324) : ((74, 65, 8), ),	}
	def __init__(self):
		super(ObtainLoginResource, self).__init__()
		self.key = StateKey.obtainLoginResource
		self.transition.update({
			Transitions.obtainResource : (
				{StateKey.home, }, 
				(350, 291, 2)
			),
		})
