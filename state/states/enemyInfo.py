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
			},
			Signals.stage61aExistsCVL : {
				(1169, 1244) : ((51, 50, 37, 255), ),
				(1117, 997) : ((32, 34, 36, 255), ),
				(172, 439) : ((168, 169, 176, 255), ),
				(428, 501) : ((185, 107, 171, 255), ),
				(885, 438) : ((86, 86, 98, 255), ),
				(853, 695) : ((219, 213, 181, 255), ),
				(115, 917) : ((169, 163, 171, 255), ),
				(428, 1003) : ((190, 89, 104, 255), ),
			},
			Signals.stage61aExistsCLT : {
				(1169, 1244) : ((51, 50, 37, 255), ),
				(1117, 997) : ((32, 34, 36, 255), ),
				(172, 439) : ((246, 246, 246, 255), ),
				(428, 501) : ((227, 210, 201, 255), ),
				(885, 438) : ((233, 231, 231, 255), ),
				(853, 695) : ((196, 127, 169, 255), ),
				(115, 917) : ((171, 172, 171, 255), ),
				(428, 1003) : ((250, 238, 237, 255), ),
			}
		})
		self.key = StateKey.enemyInfo
		self.transition.update({
			Transitions.retreatAtEnemyInfo : ({StateKey.sailingOffCombat, }, (1883, 1333, 8)),
			Transitions.startBattleAtEnemyInfo : ({
				StateKey.selectFormation,
				StateKey.chaseOrGiveUp,
				StateKey.battleResult,
			}, (2312, 1333, 8)),
		})
