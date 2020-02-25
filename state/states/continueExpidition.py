from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ContinueExpidition(State):
	signature = {
		(1184, 89) : ((255, 255, 255, 255),),
		(1419, 131) : ((255, 255, 255, 255),),
		(939, 383) : ((142, 185, 218, 255),),
		(928, 886) : ((148, 132, 46, 255),),
	}
	def __init__(self):
		super(ContinueExpidition, self).__init__()
		self.key = StateKey.continueExpidition
		self.transition.update({
			Transitions.confirmAtContinueExpidition : ({StateKey.sailingOffExpidition, }, (983, 906, 8)),
			Transitions.cancelAtContinueExpidition : ({StateKey.sailingOffExpidition, }, (1588, 906, 8)),
		})
