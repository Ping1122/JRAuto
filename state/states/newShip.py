from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class NewShip(State):
	signature = {
		(251, 183) : ((107, 162, 206), ),
		(261, 186) : ((99, 154, 206), ),
		(348, 252) : ((156, 162, 156), ),
		(53, 87) : ((255, 255, 255), ),
	}
	def __init__(self):
		super(NewShip, self).__init__()
		self.key = StateKey.newShip
		self.transition.update({
			Transitions.confirmAtNewShip : ({
				StateKey.forwardOrRetreat,
				StateKey.flagShipSeriousDamaged,
				StateKey.sailingOffCombat,
			}, (269, 325, 2)),
			Transitions.cancelAtNewShip : ({
				StateKey.forwardOrRetreat,
				StateKey.flagShipSeriousDamaged,
				StateKey.sailingOffCombat,
			}, (433, 325, 2)),
		})
