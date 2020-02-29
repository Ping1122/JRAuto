from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class SelectFormation(State):
	signature = {
		(436, 154) : ((49, 125, 206), ),
		(549, 446) : ((33, 134, 222), ),
		(612, 309) : ((33, 134, 222), ),
		(430, 214) : ((33, 105, 181), ),
	}
	def __init__(self):
		super(SelectFormation, self).__init__()
		self.key = StateKey.selectFormation
		resultStates = {
			StateKey.chaseOrGiveUp,
			StateKey.battleResult,
		}
		self.transition.update({
			Transitions.selectSingleVertical : (
				resultStates, 
				(402, 169, 4),
			),
			Transitions.selectDoubleVertical : (
				resultStates, 
				(390, 233, 4),
			),
			Transitions.selectWheelShape : (
				resultStates,
				(380, 299, 4),
			),
			Transitions.selectTrapezoidShape : (
				resultStates, 
				(370, 367, 4),
			),
			Transitions.selectSingleHorizontal : (
				resultStates, 
				(359, 431, 4),
			),
		})
