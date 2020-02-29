from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ExpiditionResult(State):
	signature = {
		(311, 55) : ((82, 117, 123), ),
		(369, 72) : ((231, 235, 239), ),
		(311, 164) : ((181, 211, 156), ),
		(308, 183) : ((74, 117, 74), ),
	}
	def __init__(self):
		super(ExpiditionResult, self).__init__()
		self.key = StateKey.expiditionResult
		self.transition.update({
            Transitions.nextState : ({StateKey.continueExpidition, }, (637, 442, 2)),
        })


