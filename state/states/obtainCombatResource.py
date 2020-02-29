from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions
from util.fullSet import FullSet

class ObtainCombatResource(State):
	signature = {
		(221, 170) : ((82, 142, 198), ),
		(232, 168) : ((206, 227, 239), ),
		(234, 177) : ((132, 178, 214), ),
		(214, 168) : ((140, 178, 214), ),
	}
	def __init__(self):
		super(ObtainCombatResource, self).__init__()
		self.key = StateKey.obtainCombatResource
		self.transition.update({
			Transitions.confirm : (FullSet(), (351, 290, 2)),
		})

