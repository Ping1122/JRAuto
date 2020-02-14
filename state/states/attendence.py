from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class Attendence(State):
	signature = {
		(310, 382) : ( (255, 255, 255, 255), ),
		(1201, 950) : ( (217, 188, 46, 255), ),
		(1266, 920) : ( (207, 178, 43, 255), ),
		(1352, 926) : ( (211, 181, 44, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.attendence
		self.transition.update({
			Transitions.confirm : ({StateKey.obtainLoginResource,}, (1280, 929, 6)),
		})
