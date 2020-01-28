from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationQuickRepair(CombatPreparation):
	signature = {
		**CombatPreparation.signature,
		(1116, 1108) : (209, 233, 253, 255),
		(1261, 1142) : (30, 138, 240, 255),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.combatPreparationQuickRepair
		self.transition.pop(Transitions.selectQuickRepair, None)
		self.behavior.update({
			Behaviors.repairAllShips : (2195, 978, 8), 
		})
	