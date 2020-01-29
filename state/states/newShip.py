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
		super().__init__()
		self.key = StateKey.newShip
		self.transition.update({
			Transitions.confirmAtNewShip : ((StateKey.forwardOrRetreat,), (982, 909, 7), True),
			Transitions.cancelAtNewShip : ((StateKey.forwardOrRetreat,), (1587, 909, 7), False),
		})

