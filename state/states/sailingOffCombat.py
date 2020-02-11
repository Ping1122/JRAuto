from state.stateKey import StateKey
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffCombat(SailingOff):
	signature = {
		**SailingOff.signature,
		(432, 56) : ((254, 255, 255, 255),),
		(563, 53) : ((15, 126, 219, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.sailingOffCombat
		self.sign.update({
			Signals.stage1Selected : {
				(204, 749) : ((226, 202, 46, 255), ),
				(344, 726) : ((232, 219, 208, 255), ),
			},
			Signals.stage2Selected : {
				(210, 733) : ((235, 210, 46, 255), ),
				(329, 730) : ((241, 167, 167, 255), ),
			},
			Signals.stage3Selected : {
				(210, 731) : ((226, 202, 46, 255), ),
				(359, 777) : ((130, 130, 130, 255), ),
			},
			Signals.stage4Selected : {
				(187, 757) : ((196, 176, 44, 255), ),
				(359, 708) : ((222, 134, 95, 255), ),
			},
			Signals.stage5Selected : {
				(183, 744) : ((219, 196, 45, 255), ),
				(339, 748) : ((91, 153, 229, 255), ),
			},
			Signals.stage6Selected : {
				(185, 754) : ((236, 211, 46, 255), ),
				(365, 718) : ((207, 175, 153, 255), ),
			},
			Signals.stage7Selected : {
				(194, 744) : ((191, 171, 44, 255), ),
				(379, 751) : ((156, 196, 216, 255), ),
			},
			Signals.stage8Selected : {
				(182, 761) : ((177, 159, 43, 255), ),
				(369, 718) : ((237, 237, 237, 255), ),
			},
		})
		self.transition.pop(Transitions.selectCombat, None)
		self.transition.update({
			Transitions.selectStage : ({StateKey.combatPreparationStatistic, }, (1810, 1131, 10)),
		})
		self.behavior.update({
			Behaviors.incrementStage : (292, 957, 6),
			Behaviors.decrementStage : (292, 550, 6),
			Behaviors.nextMap : (2496, 740, 4),
			Behaviors.prevMap : (671, 738, 4),
		})

	def getStage(self):
		for stage in range(8):
			if self.signal[Signals(stage+33)]:
				return stage
