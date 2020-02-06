from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class ExpiditionResult(State):
	signature = {
		(1135, 94) : ((255, 255, 255, 255), ),
		(1131, 317) : ((154, 196, 98, 255), ),
		(1138, 449) : ((232, 232, 232, 255), ),
		(2471, 1350) : ((255, 255, 255, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.expiditionResult
		self.transition.update({
            Transitions.nextState : ({StateKey.continueExpidition}, (2348, 1327, 10)),
        })


