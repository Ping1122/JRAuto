from copy import copy
from state.stateKey import StateKey
from state.signals import Signals
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationQuickSupply(CombatPreparation):
	signature = copy(CombatPreparation.signature)
	signature.update({
		(218, 387) : ((123, 190, 247), ),
		(184, 382) : ((33, 142, 247), ),
	})
	def __init__(self):
		super(CombatPreparationQuickSupply, self).__init__()
		self.key = StateKey.combatPreparationQuickSupply
		self.sign.update({
			Signals.ship1NeedSupply : {
				(104, 325) : ((156, 162, 156), ),
			},
			Signals.ship2NeedSupply : {
				(186, 324) : ((156, 162, 156), ),
			},
			Signals.ship3NeedSupply : {
				(268, 324) : ((156, 162, 156), ),
			},
			Signals.ship4NeedSupply : {
				(348, 324) : ((156, 162, 156), ),
			},
			Signals.ship5NeedSupply : {
				(430, 324) : ((156, 162, 156), ),
			},
			Signals.ship6NeedSupply : {
				(511, 324) : ((156, 162, 156), ),
			},
		})
		self.transition.pop(Transitions.selectQuickSupply, None)
		self.behavior.update({
			Behaviors.supplyAllShips : (602, 346, 2),
		})

	def existsShipNeedSupply(self):
		for i in range(6):
			if not self.signal[Signals(i+12)] and self.signal[Signals(i+18)]:
				return True
		return False
