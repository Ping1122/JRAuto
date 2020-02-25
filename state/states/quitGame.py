from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class QuitGame(State):
	signature = {
		(1359, 636) : ((174, 174, 174, 255), ),
        (1412, 673) : ((209, 209, 209, 255), ),
        (946, 887) : ((180, 159, 44, 255), ),
        (853, 384) : ((178, 206, 228, 255), ),
	}
	def __init__(self):
		super(QuitGame, self).__init__()
		self.key = StateKey.quitGame
		self.transition.update({
			Transitions.confirm : ({StateKey.gameClosed, }, (981, 906, 8)),
		})
