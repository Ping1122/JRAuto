from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class QuitGame(State):
	signature = {
		(238, 183) : ((99, 154, 198), ),
		(239, 194) : ((123, 170, 206), ),
		(337, 252) : ((132, 130, 132), ),
		(385, 260) : ((8, 8, 8), ),
	}
	def __init__(self):
		super(QuitGame, self).__init__()
		self.key = StateKey.quitGame
		self.transition.update({
			Transitions.confirm : (
				{StateKey.gameClosed, }, 
				(269, 326, 3)
			),
		})
