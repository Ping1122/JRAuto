from state.state import State
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class NewsAndAnnouncement(State):
	signature = {
		(51, 476) : ((57, 56, 57), ),
		(34, 476) : ((57, 56, 57), ),
		(63, 481) : ((255, 255, 255), ),
		(614, 50) : ((255, 255, 255), ),
	}
	def __init__(self):
		super(NewsAndAnnouncement, self).__init__()
		self.key = StateKey.newsAndAnnouncement
		self.transition.update({
			Transitions.close : ({StateKey.attendence, StateKey.home}, (22, 58, 3)),
		})
		self.behavior.update({
			Behaviors.checkNoNewsToday: (43, 485, 2),
		})
