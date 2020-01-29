from state.state import State
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class NewsAndAnnouncement(State):
	signature = {
		(441, 1347) : ((253, 253, 253, 255),),
		(315, 1340) : ((251, 251, 251, 255),),
		(2327, 86) : ((255, 255, 255, 255),),
		(69, 76) : ((193, 193, 193, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.NewsAndAnnouncement
		self.transition.update({
			Transitions.close : ((StateKey.attendence,), (79, 75, 8), False),	
		})
		self.behavior.update({
			Behaviors.checkNoNewsToday: (156, 1339, 8),
		})
