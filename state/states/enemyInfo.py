from state.state import State
from state.signals import Signals
from state.stateKey import StateKey
from state.transitions import Transitions

class EnemyInfo(State):
	signature = {
		(61, 79) : ((255, 255, 255), ),
		(507, 475) : ((123, 44, 49), ),
		(517, 477) : ((255, 255, 255), ),
		(655, 478) : ((165, 150, 41), ),
	}

	def __init__(self):
		super(EnemyInfo, self).__init__()
		self.sign.update({
			Signals.stage74bExistsSubmarine : {
				(572, 219) : ((16, 24, 33), ),
				(244, 152) : ((57, 56, 57), ),
				(505, 150) : ((57, 40, 24), ),
				(38, 335) : ((90, 93, 107), ),
				(112, 345) : ((140, 44, 49), ),
			},
			Signals.stage61aExistsCVL : {
				(295, 57) : ((49, 60, 66), ),
				(307, 57) : ((24, 44, 57), ),
				(291, 409) : ((57, 40, 24), ),
				(48, 211) : ((82, 69, 107), ),
				(87, 219) : ((57, 52, 57), ),
			},
			Signals.stage61aExistsCLT : {
				(295, 57) : ((49, 60, 66), ),
				(307, 57) : ((24, 44, 57), ),
				(291, 409) : ((57, 40, 24), ),
				(26, 335) : ((214, 121, 173), ),
				(47, 331) : ((148, 60, 148), ),
			},
			Signals.stage55bossSquardAtA : {
				(315, 61) : ((41, 52, 57), ),
				(297, 56) : ((41, 52, 57), ),
				(479, 321) : ((57, 20, 16), ),
			},
			Signals.stage55bossSquardAtB : {
				(315, 61) : ((41, 52, 57), ),
				(297, 56) : ((41, 52, 57), ),
				(551, 404) : ((66, 40, 24), ),
			},
			Signals.stage81aExistsCL : {
				(292, 56) : ((49, 60, 66), ),
				(309, 65) : ((16, 36, 49), ),
				(149, 247) : ((57, 36, 16), ),
				(106, 376) : ((16, 16, 24), ),
				(39, 266) : ((231, 223, 214), ),
			},
			Signals.stage81aExistsCA : {
				(292, 56) : ((49, 60, 66), ),
				(309, 65) : ((16, 36, 49), ),
				(149, 247) : ((57, 36, 16), ),
				(51, 202) : ((222, 219, 222), ),
				(328, 201) : ((115, 113, 115), ),
			}
		})
		self.key = StateKey.enemyInfo
		self.transition.update({
			Transitions.retreatAtEnemyInfo : (
				{StateKey.sailingOffCombat, }, 
				(515, 483, 3)),
			Transitions.startBattleAtEnemyInfo : ({
				StateKey.selectFormation,
				StateKey.chaseOrGiveUp,
				StateKey.battleResult,
			}, (632, 483, 3)),
		})
