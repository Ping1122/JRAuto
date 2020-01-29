from state.state import State
from state.stateKey import StateKey
from state.signals import Signals
from state.transitions import Transitions

class SailingOff(State):
	signature = {
		(17, 1419) : ((15, 23, 42, 255),),
		(2421, 1405) : ((12, 28, 47, 255),),
		(69, 74) : ((191, 192, 196, 255),),
		(2246, 1391) : ((12, 32, 57, 255),),
	}	
	def __init__(self):
		super().__init__()
		self.sign.update({
			Signals.existsCompletedExpidition : {
				(1254, 25) : ((255, 254, 254, 255),),
				(1241, 26) : ((255, 44, 28, 255),),		
			}
		})
		self.transition.update({
			Transitions.backAtSailingOff : ((StateKey.home,), (81, 74, 7), False),
			Transitions.selectCombat : ((StateKey.sailingOffCombat,), (461, 62, 6), False),
			Transitions.selectExercise : ((StateKey.sailingOffExercise,), (798, 62, 6), False),
			Transitions.selectExpidition : ((StateKey.sailingOffExpidition,), (1122, 62, 6), False),
			Transitions.selectCampaign : ((StateKey.sailingOffCampaign,), (1465, 62, 6), False),
		})