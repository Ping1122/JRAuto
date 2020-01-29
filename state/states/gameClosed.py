from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class GameClosed(State):
	signature = {
		(52, 46) : ((15, 17, 21, 255),),
		(132, 1258) : ((22, 24, 30, 255),),
		(2470, 214) : ((23, 25, 31, 255),),
		(2422, 1308) : ((21, 23, 28, 255),),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.gameClosed	
		self.transition.update({
			Transitions.startGame : ((StateKey.login,), (1286, 310, 10), False), 
		})