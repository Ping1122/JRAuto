from state.state import State
from state.signals import Signals
from state.stateKey import StateKey
from state.transitions import Transitions

class ForwardOrRetreat(State):
	signature = {
		(261, 271) : ((74, 117, 74), ),
		(261, 296) : ((132, 162, 99), ),
		(239, 329) : ((189, 93, 90), ),
		(232, 335) : ((198, 130, 132), ),
		(249, 332) : ((247, 243, 247), ),
		(453, 330) : ((189, 223, 255), ),
	}
	def __init__(self):
		super(ForwardOrRetreat, self).__init__()
		self.key = StateKey.forwardOrRetreat
		self.sign.update({
			Signals.existsSeriouslyDamagedShip : {
				(223, 216) : ((255, 203, 74), ),			
			}
		})
		self.transition.update({
			Transitions.forward : ({
				StateKey.enemyInfo,
				StateKey.selectFormation,
				StateKey.chaseOrGiveUp,
				StateKey.battleResult,
				StateKey.home,
			}, (241, 335, 2)),
			Transitions.retreatAtForwardOrRetreat : (
				{StateKey.sailingOffCombat,}, 
				(459, 334, 2),
			),
		})
