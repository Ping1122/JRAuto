from states.state import State
from states.sailingOffState import SailingOffState

class HomeState(State):
	signature = {
		(1404, 760) : (140, 149, 153, 255),
		(1170, 744) : (255, 145, 118, 255),
		(986, 751) : (54, 129, 201, 255),
		(73, 743) : (255, 255, 255, 255),
		(1388, 668) : (67, 67, 67, 255),
		(73, 797) : (0, 160, 233, 255),
	}
	def __init__(self):
		super().__init__()
		self.transition = {
			(1406, 754, 8) : {SailingOffState}
		}