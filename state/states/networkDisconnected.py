from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions
from util.fullSet import FullSet

class NetworkDisconnected(State):
	signature = {
		(226, 191) : ((57, 125, 189), ),
		(243, 245) : ((181, 182, 181), ),
		(295, 250) : ((148, 154, 148), ),
		(463, 243) : ((189, 195, 189), ),
	}
	def __init__(self):
		super(NetworkDisconnected, self).__init__()
		self.key = StateKey.networkDisconnected
		self.transition.update({
			Transitions.confirm : (FullSet(), (269, 326, 2)),
		})
