from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions
from util.fullSet import FullSet

class ObtainCombatResource(State):
	signature = {
		(817, 370) : ((137, 179, 214, 255), ),
		(855, 386) : ((129, 175, 213, 255), ),
		(1239, 800) : ((148, 200, 250, 255), ),
		(1315, 813) : ((92, 171, 245, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.obtainCombatResource
		self.transition.update({
			Transitions.confirm : (FullSet(), (1282, 800, 6)),
		})

