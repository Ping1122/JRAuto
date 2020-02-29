from copy import copy
from state.stateKey import StateKey
from state.signals import Signals
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationStatistic(CombatPreparation):
	signature = copy(CombatPreparation.signature)
	signature.update({
		(123, 388) : ((41, 146, 239), ),
		(93, 388) : ((33, 138, 239), ),
	})
	def __init__(self):
		super(CombatPreparationStatistic, self).__init__()
		self.sign.update({
			Signals.strategyEnabled: {
				(449, 134) : ((247, 186, 57), ),
			},
			Signals.strategyDisabled: {
				(449, 134) : ((41, 150, 255), ),
			},
			Signals.strategyExhausted: {
				(449, 134) : ((148, 146, 148), ),
			}
		})
		self.key = StateKey.combatPreparationStatistic
		self.transition.pop(Transitions.selectStatistic, None)
		self.transition.update({
			Transitions.selectStrategy: ({StateKey.strategy, }, (458, 142, 2)),
		})
