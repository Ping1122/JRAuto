from copy import copy
from state.signals import Signals
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions
from state.states.sailingOff import SailingOff

class SailingOffCombat(SailingOff):
	signature = copy(SailingOff.signature)
	signature.update({
		(118, 52) : ((255, 255, 255), ),
		(106, 55) : ((16, 134, 231), ),
	})
	def __init__(self):
		super(SailingOffCombat, self).__init__()
		self.key = StateKey.sailingOffCombat
		self.sign.update({
			Signals.stage1Selected : {
				(100, 287) : ((74, 69, 57), ),
				(130, 286) : ((115, 166, 214), ),
			},
			Signals.stage2Selected : {
				(100, 287) : ((239, 186, 181), ),
				(130, 286) : ((239, 170, 156), ),
			},
			Signals.stage3Selected : {
				(100, 287) : ((181, 154, 107), ),
				(130, 286) : ((57, 109, 115), ),
			},
			Signals.stage4Selected : {
				(100, 287) : ((165, 243, 247), ),
				(130, 286) : ((247, 195, 140), ),
			},
			Signals.stage5Selected : {
				(100, 287) : ((239, 243, 247), ),
				(130, 286) : ((99, 170, 222), )
			},
			Signals.stage6Selected : {
				(100, 287) : ((165, 162, 165), ),
				(130, 286) : ((115, 162, 198), ),
			},
			Signals.stage7Selected : {
				(100, 287) : ((123, 211, 255), ),
				(130, 286) : ((156, 158, 173), ),
			},
			Signals.stage8Selected : {
				(100, 287) : ((66, 117, 82), ),
				(130, 286) : ((57, 105, 90), ),
			},
		})
		self.transition.pop(Transitions.selectCombat, None)
		self.transition.update({
			Transitions.selectStage : (
				{StateKey.combatPreparationStatistic, }, 
				(496, 391, 2)
			),
		})
		self.behavior.update({
			Behaviors.incrementStage : (79, 341, 2),
			Behaviors.decrementStage : (79, 229, 2),
			Behaviors.nextMap : (677, 283, 1),
			Behaviors.prevMap : (178, 283, 1),
		})

	def getStage(self):
		for stage in range(8):
			if self.signal[Signals(stage+33)]:
				return stage
