from states.state import State
from states.sailingOffState import SailingOffState

class SailingOffState(State):
	signature = {
		(1453, 36) : (14, 17, 32, 255),
		(1219, 74) : (55, 68, 88, 255),
		(1326, 780) : (88, 100, 117, 255),
		(49, 778) : (67, 77, 88, 255),
		(1479, 409) : (17, 38, 59, 255),
		(44, 14) : (84, 86, 96, 255),
	}
	def __init__(self):
		super().__init__()
		self.transition = {
			(1406, 754, 8) : {SailingOffState}
		}