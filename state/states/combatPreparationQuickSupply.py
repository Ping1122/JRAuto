from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationQuickSupply(CombatPreparation):
	signature = {
		**CombatPreparation.signature,
		(678, 1099) : (35, 145, 248, 255),
		(890, 1128) : (151, 202, 249, 255),	
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.combatPreparationQuickSupply
		self.transition.pop(Transitions.selectQuickSupply, None)
		self.behavior.update({
			Behaviors.supplyAllShips : (2195, 978, 8), 
		})
	