from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class FlagShipSeriousDamaged(State):
	signature = {
		(509, 332) : ((107, 20, 24), ),
		(495, 319) : ((198, 158, 156), ),
		(491, 320) : ((140, 56, 57), ),
		(470, 320) : ((247, 235, 239), ),

	}
	def __init__(self):
		super(FlagShipSeriousDamaged, self).__init__()
		self.key = StateKey.flagShipSeriousDamaged
		self.transition.update({
			Transitions.retreatAtFlagShipSeriousDamaged : ({StateKey.home, }, (479, 318, 3)),
		})
