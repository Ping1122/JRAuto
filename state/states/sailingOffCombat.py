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
		self.transition.pop(Transitions.selectCombat, None)
		self.transition.update({
			Transitions.selectStage : ((StateKey.combatPreparationStatistic,), (1628, 750, 20), False),
		})
