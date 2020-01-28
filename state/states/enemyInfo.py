from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class EnemyInfo(State):
	signature = {
		(152, 180) : (255, 255, 255, 255),
		(1930, 1318) : (255, 255, 255, 255),
		(1910, 1326) : (255, 255, 255, 255),
		(2405, 1355) : (0, 0, 0, 255),
	}
	
	def __init__(self):
		super().__init__()
		self.sign.update({
			"stage74bExistSubmarine" : {
				(1276, 53) : (15, 37, 56, 255),
				(1289, 87) : (46, 57, 64, 255),
				(1346, 77) : (26, 44, 59, 255),
				(1321, 73) : (36, 51, 62, 255),	
				(66, 893) : (76, 77, 83, 255),
				(145, 935) : (117, 120, 133, 255),
				(429, 961) : (203, 189, 192, 255),
				(404, 977) : (159, 21, 65, 255),
			}
		})
		self.key = StateKey.enemyInfo
		self.transition.update({
			Transitions.retreatAtEnemyInfo : ((StateKey.sailingOffCombat,), (1883, 1333, 8), False),
			Transitions.startBattleAtEnemyInfo : ((StateKey.selectFormation,), (2312, 1333, 8), False),
		})