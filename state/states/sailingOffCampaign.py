from copy import copy
from state.stateKey import StateKey
from state.transitions import Transitions
from state.behaviors import Behaviors
from state.signals import Signals
from state.states.sailingOff import SailingOff

class SailingOffCampaign(SailingOff):
	signature = copy(SailingOff.signature)
	signature.update({
		(388, 56) : ((165, 211, 247), ),
		(381, 55) : ((16, 134, 231), ),
	})
	def __init__(self):
		super(SailingOffCampaign, self).__init__()
		self.key = StateKey.sailingOffCampaign
		self.sign.update({
			Signals.campaignNormalMode: {
				(523, 134) : ((214, 235, 255), ),
				(536, 134) : ((247, 251, 255), ),
			},
			Signals.campaignHardMode: {
				(523, 134) : ((140, 56, 49), ),
				(536, 134) : ((255, 251, 247), ),
			},
			Signals.noMoreCampaignTrials: {
				(521, 408) : ((231, 231, 231), ),
				(522, 409) : ((198, 199, 198), ),
			}
		})
		self.transition.pop(Transitions.selectCampaign, None)
		self.transition.update({
			Transitions.selectDestroyerCampaign : (
				{StateKey.combatPreparationStatistic, }, 
				(82, 269, 10)
			),
			Transitions.selectCuriserCampaign : (
				{StateKey.combatPreparationStatistic, }, 
				(213, 269, 10)
			),
			Transitions.selectBattleShipCampaign : (
				{StateKey.combatPreparationStatistic, }, 
				(347, 269, 10)
			),
			Transitions.selectAricraftCarrierCampaign : (
				{StateKey.combatPreparationStatistic, }, 
				(482, 269, 10)
			),
			Transitions.selectSubmarineCampaign : (
				{StateKey.combatPreparationStatistic, }, 
				(621, 269, 10)
			),
		})
		self.behavior.update({
			Behaviors.switchMode: (552, 135, 1),
		})
