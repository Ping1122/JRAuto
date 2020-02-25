from copy import copy
from state.stateKey import StateKey
from state.signals import Signals
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationQuickSupply(CombatPreparation):
	signature = copy(CombatPreparation.signature)
	signature.update({
		(678, 1099) : ((35, 145, 248, 255), ),
		(890, 1128) : ((151, 202, 249, 255), ),
	})
	def __init__(self):
		super(CombatPreparationQuickSupply, self).__init__()
		self.key = StateKey.combatPreparationQuickSupply
		self.sign.update({
			Signals.ship1NeedSupply : {
				(379, 996) : ((160, 160, 160, 255), ),
			},
			Signals.ship2NeedSupply : {
				(975, 993) : ((160, 160, 160, 255), ),
			},
			Signals.ship3NeedSupply : {
				(1274, 997) : ((160, 160, 160, 255), ),
			},
			Signals.ship4NeedSupply : {
				(1571, 996) : ((160, 160, 160, 255), ),
			},
			Signals.ship5NeedSupply : {
				(1572, 944) : ((160, 160, 160, 255), ),
			},
			Signals.ship6NeedSupply : {
				(1867, 943) : ((160, 160, 160, 255), ),
			},
		})
		self.transition.pop(Transitions.selectQuickSupply, None)
		self.behavior.update({
			Behaviors.supplyAllShips : (2195, 978, 8),
		})

	def existsShipNeedSupply(self):
		for i in range(6):
			if not self.signal[Signals(i+12)] and self.signal[Signals(i+18)]:
				return True
		return False
