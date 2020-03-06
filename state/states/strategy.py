from state.state import State
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class Strategy(State):
	signature = {
		(569, 482) : ((156, 134, 33), ),
		(641, 485) : ((16, 20, 16), ),
		(45, 389) : ((24, 32, 41), ),
		(53, 484) : ((8, 16, 33), ),
	}
	def __init__(self):
		super(Strategy, self).__init__()
		self.key = StateKey.strategy
		self.transition.update({
			Transitions.backToCombatPreparation : (
				{StateKey.combatPreparationStatistic, }, 
				(435, 459, 4)
			),
		})
		self.behavior.update({
			Behaviors.switchStrategy : (540, 282, 2),
		})
