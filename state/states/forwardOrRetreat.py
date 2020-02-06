from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ForwardOrRetreat(State):
	signature = {
		(790, 602) : ((177, 177, 177, 255),),
		(955, 780) : ((230, 230, 230, 255),),
		(847, 919) : ((224, 174, 174, 255),),
		(928, 926) : ((212, 144, 144, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.forwardOrRetreat
		self.transition.update({
			Transitions.forward : ({
				StateKey.enemyInfo,
				StateKey.selectFormation,
				StateKey.chaseOrGiveUp,
				StateKey.battleResult,
			}, (885, 938, 7)),
			Transitions.retreatAtForwardOrRetreat : ({StateKey.sailingOffCombat,}, (1677, 938, 7)),
		})
