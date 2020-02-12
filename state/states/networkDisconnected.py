from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class NetworkDisconnected(State):
	signature = {
		(1036, 391) : ((13, 108, 183, 255), ),
        (1136, 648) : ((198, 198, 198, 255), ),
        (1415, 694) : ((174, 174, 174, 255), ),
        (931, 908) : ((196, 224, 252, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.networkDisconnected
		self.behavior.update({
			Behaviors.confirm : (987, 911, 8)
		})
