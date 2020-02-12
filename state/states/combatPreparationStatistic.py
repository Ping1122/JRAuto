from state.stateKey import StateKey
from state.signals import Signals
from state.transitions import Transitions
from state.states.combatPreparation import CombatPreparation

class CombatPreparationStatistic(CombatPreparation):
	signature = {
		**CombatPreparation.signature,
		(448, 1132) : ((31, 140, 242, 255), ),
		(525, 1120) : ((254, 255, 255, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.sign.update({
			Signals.strategyEnabled: {
				(1644, 260) : ((235, 175, 44, 255), ),
			},
			Signals.strategyDisabled: {
				(1644, 266) : ((39, 149, 253, 255), ),
			},
			Signals.strategyExhausted: {
				(1644, 266) : ((146, 146, 146, 255), ),
			}
		})
		self.key = StateKey.combatPreparationStatistic
		self.transition.pop(Transitions.selectStatistic, None)
		self.transition.update({
			Transitions.selectStrategy: ({StateKey.strategy, }, (1675, 237, 5)),
		})
