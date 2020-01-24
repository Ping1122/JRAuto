from states.state import State

class GameCloseState(State):
	signature = {
		(98, 188) : (31, 33, 41, 255),
		(634, 178) : (36, 39, 48, 255),
		(1356, 186) : (29, 31, 40, 255),
		(214, 552) : (33, 35, 44, 255),
		(730, 534) : (34, 37, 48, 255),
		(1426, 576) : (32, 35, 43, 255)
	}

	def __init__(self):
		super().__init__()
		self.transit