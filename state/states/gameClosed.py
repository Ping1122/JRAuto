from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class GameClosed(State):
	signature = {
		(104, 144) : ((241, 208, 186), ),
		(48, 445) : ((26, 28, 35), ),
		(664, 458) : ((44, 45, 52), ),
		(376, 503) : ((20, 20, 26), ),
	}
	def __init__(self):
		super(GameClosed, self).__init__()
		self.key = StateKey.gameClosed
		self.transition.update({
			Transitions.startGame : ({StateKey.login, }, (108, 137, 3)),
		})
