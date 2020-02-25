from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class NewShip(State):
	signature = {
		(1085, 561) : ((225, 225, 225, 255),),
		(143, 124) : ((255, 255, 255, 255),),
		(468, 186) : ((255, 255, 255, 255),),
		(1519, 679) : ((195, 195, 195, 255),),
	}
	def __init__(self):
		super(NewShip, self).__init__()
		self.key = StateKey.newShip
		self.transition.update({
			Transitions.confirmAtNewShip : ({
				StateKey.forwardOrRetreat,
				StateKey.flagShipSeriousDamaged,
				StateKey.sailingOffCombat,
			}, (982, 909, 7)),
			Transitions.cancelAtNewShip : ({
				StateKey.forwardOrRetreat,
				StateKey.flagShipSeriousDamaged,
				StateKey.sailingOffCombat,
			}, (1587, 909, 7)),
		})
