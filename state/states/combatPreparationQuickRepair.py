from copy import copy
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationQuickRepair(CombatPreparation):
	signature = copy(CombatPreparation.signature)
	signature.update({
		(311, 388) : ((33, 138, 239), ),
		(276, 386) : ((33, 142, 247), ),
	})
	def __init__(self):
		super(CombatPreparationQuickRepair, self).__init__()
		self.key = StateKey.combatPreparationQuickRepair
		self.transition.pop(Transitions.selectQuickRepair, None)
		self.behavior.update({
			Behaviors.repairAllShips : (600, 346, 2),
			Behaviors.repairShip1 : (72, 248, 6),
			Behaviors.repairShip2 : (155, 248, 6),
			Behaviors.repairShip3 : (233, 248, 6),
			Behaviors.repairShip4 : (316, 248, 6),
			Behaviors.repairShip5 : (395, 248, 6),
			Behaviors.repairShip6 : (479, 248, 6),
		})
