from state.state import State
from state.signals import Signals
from state.stateKey import StateKey
from state.transitions import Transitions

class EnemyInfo(State):
	signature = {
		(152, 180) : ((255, 255, 255, 255),),
		(1930, 1318) : ((255, 255, 255, 255),),
		(1910, 1326) : ((255, 255, 255, 255),),
		(2405, 1355) : ((0, 0, 0, 255),),
	}
	
	def __init__(self):
		super().__init__()
		self.sign.update({
			Signals.stage74bExistsSubmarine : {
				(1829, 171) : ((32, 39, 42, 255),),
				(1882, 213) : ((51, 52, 40, 255),),		
				(62, 932) : ((95, 96, 110, 255),),
				(407, 973) : ((95, 25, 28, 255),),
			}
		})
		self.key = StateKey.enemyInfo
		self.transition.update({
			Transitions.retreatAtEnemyInfo : ((StateKey.sailingOffCombat,), (1883, 1333, 8), False),
			Transitions.startBattleAtEnemyInfo : ((StateKey.selectFormation,), (2312, 1333, 8), False),
		})