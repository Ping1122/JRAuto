from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ContinueExpidition(State):
	signature = {
		(235, 182) : ((90, 146, 198), ),
		(257, 185) : ((123, 174, 214), ),
		(415, 252) : ((123, 125, 123), ),
		(383, 251) : ((181, 186, 181), ),
	}
	def __init__(self):
		super(ContinueExpidition, self).__init__()
		self.key = StateKey.continueExpidition
		self.transition.update({
			Transitions.confirmAtContinueExpidition : (
				{StateKey.sailingOffExpidition, }, 
				(269, 325, 3)
			),
			Transitions.cancelAtContinueExpidition : (
				{StateKey.sailingOffExpidition, }, 
				(434, 326, 3)
			),
		})
