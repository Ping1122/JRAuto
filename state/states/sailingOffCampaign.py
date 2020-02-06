from state.stateKey import StateKey
from state.transitions import Transitions
from state.behaviors import Behaviors
from state.signals import Signals
from state.states.sailingOff import SailingOff

class SailingOffCampaign(SailingOff):
	signature = {
		**SailingOff.signature,
		(1456, 63) : ((16, 132, 228, 255),),
		(1410, 40) : ((200, 227, 249, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.sailingOffCampaign
		self.sign.update({
			Signals.campaignNormalMode: {
				(2007, 177) : ((141, 51, 51, 255), ),
				(2129, 233) : ((141, 51, 51, 255), ),
			},
			Signals.campaignHardMode: {
				(2130, 183) : ((39, 148, 252, 255), ),
				(2137, 236) : ((28, 136, 237, 255), ),
			},
			Signals.noMoreCampaignTrials: {
				(438, 1199) : ((187, 187, 187, 255), ),
				(453, 1209) : ((191, 191, 191, 255), ),
			}
		})
		self.transition.pop(Transitions.selectCampaign, None)
		self.transition.update({
			Transitions.selectDestroyerCampaign : ({StateKey.combatPreparationStatistic, }, (293, 716, 20)),
			Transitions.selectCuriserCampaign : ({StateKey.combatPreparationStatistic, }, (805, 716, 20)),
			Transitions.selectBattleShipCampaign : ({StateKey.combatPreparationStatistic, }, (1293, 716, 20)),
			Transitions.selectAricraftCarrierCampaign : ({StateKey.combatPreparationStatistic, }, (1765, 716, 20)),
			Transitions.selectSubmarineCampaign : ({StateKey.combatPreparationStatistic, }, (2279, 716, 20)),
		})
		self.behavior.update({
			Behaviors.switchMode: (1999, 212, 4),
		})
