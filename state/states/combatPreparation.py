from state.state import State
from state.signals import Signals
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class CombatPreparation(State):
	signature = {
		(247, 47) : ((255, 255, 255, 255),),
		(437, 64) : ((255, 255, 255, 255),),
		(2080, 1335) : ((255, 218, 48, 255),),
		(2343, 1347) : ((97, 87, 38, 255),),
	}

	def __init__(self):
		super().__init__()
		self.sign.update({
			Signals.ship1Intact : {
				(138, 856) : ((64, 162, 110, 255), ),
				(149, 854) : ((79, 169, 121, 255), ),
			},
			Signals.ship2Intact : {
				(434, 854) : ((63, 161, 108, 255), ),
				(445, 854) : ((85, 172, 126, 255), ),
			},
			Signals.ship3Intact : {
				(734, 855) : ((63, 161, 108, 255), ),
				(742, 854) : ((84, 171, 124, 255), ),
			},
			Signals.ship4Intact : {
				(1025, 850) : ((86, 172, 126, 255), ),
				(1031, 854) : ((63, 161, 108, 255), ),
			},
			Signals.ship5Intact : {
				(1325, 850) : ((85, 172, 125, 255), ),
				(1329, 854) : ((63, 161, 108, 255), ),
			},
			Signals.ship6Intact : {
				(1625, 854) : ((64, 161, 109, 255), ),
				(1638, 852) : ((86, 172, 126, 255), ),
			},
			Signals.slot1Empty : {
				(261, 649) : ((188, 191, 194, 255), ),
				(262, 719) : ((47, 86, 117, 255), ),
			},
			Signals.slot2Empty: {
				(560, 672) : ((188, 193, 194, 255), ),
				(562, 721) : ((50, 90, 122, 255), ),
			},
			Signals.slot3Empty : {
				(895, 648) : ((188, 192, 194, 255), ),
				(860, 729) : ((49, 93, 123, 255), ),
			},
			Signals.slot4Empty: {
				(1159, 644) : ((188, 192, 195, 255), (235, 240, 244, 255),),
				(1157, 722) : ((49, 91, 124, 255), (61, 114, 155, 255),),
			},
			Signals.slot5Empty : {
				(1459, 647) : ((188, 192, 195, 255), (235, 240, 244, 255),),
				(1459, 716) : ((49, 91, 123, 255), (61, 113, 153, 255), ),
			},
			Signals.slot6Empty: {
				(1758, 646) : ((188, 192, 194, 255), (235, 240, 243, 255),),
				(1757, 732) : ((50, 94, 125, 255), (62, 117, 156, 255),)
			},
			Signals.ship1NeedSupply : {
				(379, 996) : ((160, 160, 160, 255), ),
			},
			Signals.ship2NeedSupply : {
				(975, 993) : ((160, 160, 160, 255), ),
			},
			Signals.ship3NeedSupply : {
				(1274, 997) : ((160, 160, 160, 255), ),
			},
			Signals.ship4NeedSupply : {
				(1571, 996) : ((160, 160, 160, 255), ),
			},
			Signals.ship5NeedSupply : {
				(1572, 944) : ((160, 160, 160, 255), ),
			},
			Signals.ship6NeedSupply : {
				(1867, 943) : ((160, 160, 160, 255), ),
			},
		})
		self.transition.update({
			Transitions.selectStatistic : ({StateKey.combatPreparationStatistic, }, (447, 1133, 8)),
			Transitions.selectQuickSupply : ({StateKey.combatPreparationQuickSupply, }, (789, 1133, 8)),
			Transitions.selectQuickRepair : ({StateKey.combatPreparationQuickRepair, }, (1138, 1133, 8)),
			Transitions.backAtCombatPreparation : ({StateKey.sailingOffCombat, }, (77, 74, 8)),
			Transitions.startBattleAtCombatPreparation : ({
				StateKey.enemyInfo,
				StateKey.selectFormation,
				StateKey.chaseOrGiveUp,
				StateKey.battleResult,
			}, (2234, 1317, 8)),
		})
		self.behavior.update({
			Behaviors.selectSquardon1 : (272, 231, 8),
			Behaviors.selectSquardon2 : (589, 231, 8),
			Behaviors.selectSquardon3 : (906, 231, 8),
			Behaviors.selectSquardon4 : (1220, 231, 8),
		})

	def getDamagedShips(self):
		damagedShips = []
		for i in range(6):
			if not self.signal[Signals(i)] and not self.signal[Signals(i+12)]:
				damagedShips.append(i+1)
		return damagedShips

	def existsShipNeedSupply(self):
		for i in range(6):
			if not self.signal[Signals(i+12)] and self.signal[Signals(i+18)]:
				return True
		return False
