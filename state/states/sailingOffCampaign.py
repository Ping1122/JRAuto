from state.stateKey import StateKey
from state.transitions import Transitions
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
		self.transition.pop(Transitions.selectCampaign, None)
		self.transition.update({
		})