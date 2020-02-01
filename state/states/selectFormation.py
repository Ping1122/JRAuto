from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class SelectFormation(State):
	signature = {
		(1486, 251) : ((255, 255, 255, 255),),
		(1417, 524) : ((255, 255, 255, 255),),
		(2244, 863) : ((30, 135, 220, 255),),
		(2476, 1339) : ((30, 135, 220, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.selectFormation
		resultStates = (
			StateKey.chaseOrGiveUp,
			StateKey.forwardOrRetreat,
			StateKey.newShip,
			StateKey.SailingOffCombat
		)
		self.transition.update({
			Transitions.selectSingleVertical : (resultStates, (1496, 327, 10), True),
			Transitions.selectDoubleVertical : (resultStates, (1430, 564, 10), True),
			Transitions.selectWheelShape : (resultStates, (1392, 805, 10), True),
			Transitions.selectTrapezoidShape : (resultStates, (1347, 1052, 10), True),
			Transitions.selectSingleHorizontal : (resultStates, (1309, 1295, 10), True),
		})