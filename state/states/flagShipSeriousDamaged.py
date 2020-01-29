from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class FlagShipSeriousDamaged(State):
	signature = {
		(1255, 520) : ((130, 33, 33, 255), ),
		(1335, 510) : ((130, 33, 33, 255), ),
		(1380, 514) : ((130, 33, 33, 255), ),
		(1699, 874) : ((255, 255, 255, 255), ),

	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.flagShipSeriousDamaged
		self.transition.update({
			Transitions.retreatAtFlagShipSeriousDamaged : ((StateKey.home, ), (1755, 882, 8), False),
		})

