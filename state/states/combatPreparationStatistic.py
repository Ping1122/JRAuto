from state.stateKey import StateKey
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationStatistic(CombatPreparation):
	signature = {
		**CombatPreparation.signature,
		(448, 1132) : (31, 140, 242, 255),
		(525, 1120) : (254, 255, 255, 255),	
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.combatPreparationStatistic
		self.transition.pop(Transitions.selectStatistic, None)
