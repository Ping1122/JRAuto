from state.state import State
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class Strategy(State):
	signature = {
		(2054, 1353) : ((155, 134, 30, 255), ),
		(140, 1236) : ((14, 23, 34, 255), ),
		(2053, 161) : ((13, 23, 38, 255), ),
		(148, 213) : ((11, 14, 26, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.strategy
		self.transition.update({
			Transitions.backToCombatPreparation : ({StateKey.combatPreparationStatistic, }, (1598, 1194, 8)),
		})
		self.behavior.update({
			Behaviors.switchStrategy : (1987, 744, 8),
		})
