from state.state import State
from state.stateKey import StateKey
from state.signals import Signals
from state.transitions import Transitions

class SailingOff(State):
	signature = {
		(37, 54) : ((189, 195, 198), ),
		(446, 56) : ((16, 28, 49), ),
		(512, 68) : ((16, 28, 49), ),
		(592, 60) : ((16, 16, 33), ),
	}
	def __init__(self):
		super(SailingOff, self).__init__()
		self.sign.update({
			Signals.existsCompletedExpidition : {
				(345, 46) : ((255, 44, 24), ),
				(343, 44) : ((255, 247, 247), ),
			},
		})
		self.transition.update({
			Transitions.backAtSailingOff : (
				{StateKey.home, }, 
				(21, 58, 2)
			),
			Transitions.selectCombat : (
				{StateKey.sailingOffCombat, }, 
				(126, 52, 2)
			),
			Transitions.selectExercise : (
				{StateKey.sailingOffExercise, }, 
				(218, 52, 2)
			),
			Transitions.selectExpidition : (
				{StateKey.sailingOffExpidition, }, 
				(306, 52, 2)
			),
			Transitions.selectCampaign : (
				{StateKey.sailingOffCampaign, }, 
				(398, 52, 2)
			),
		})
