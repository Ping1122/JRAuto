from state.state import State
from state.signals import Signals
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class CombatPreparation(State):
	signature = {
		(118, 49) : ((107, 109, 115), ),
		(102, 49) : ((140, 142, 148), ),
		(91, 48) : ((41, 44, 57), ),
		(66, 56) : ((41, 40, 57), ),
	}

	def __init__(self):
		super(CombatPreparation, self).__init__()
		self.sign.update({
			Signals.ship1Intact : {
				(37, 311) : ((66, 162, 107), ),
				(36, 310) : ((82, 170, 123), ),
			},
			Signals.ship2Intact : {
				(118, 310) : ((82, 170, 123), ),
				(120, 310) : ((66, 162, 107), ),
			},
			Signals.ship3Intact : {
				(200, 310) : ((82, 170, 123), ),
				(201, 310) : ((66, 162, 107), ),
			},
			Signals.ship4Intact : {
				(200, 310) : ((82, 170, 123), ),
				(201, 310) : ((66, 162, 107), ),
			},
			Signals.ship5Intact : {
				(362, 310) : ((82, 170, 123), ),
				(363, 311) : ((66, 162, 107), ),
			},
			Signals.ship6Intact : {
				(443, 310) : ((82, 170, 123), ),
				(445, 310) : ((66, 162, 107), ),
			},
			Signals.slot1Empty : {
				(71, 253) : ((189, 190, 198), ),
				(72, 297) : ((74, 117, 148), ),
			},
			Signals.slot2Empty: {
				(154, 254) : ((189, 190, 198), ),
				(153, 296) : ((82, 121, 148), ),
			},
			Signals.slot3Empty : {
				(236, 253) : ((189, 190, 198), ),
				(236, 296) : ((82, 121, 156), ),
			},
			Signals.slot4Empty: {
				(316, 253) : ((239, 239, 247), (189, 190, 198)),
				(315, 296) : ((99, 154, 198), (82, 121, 156), ),
			},
			Signals.slot5Empty : {
				(398, 253) : ((239, 239, 247), (189, 190, 198)),
				(397, 296) : ((90, 150, 189), (74, 121, 148)),
			},
			Signals.slot6Empty: {
				(479, 253) : ((239, 239, 247), (189, 190, 198)),
				(479, 296) : ((99, 154, 198), (82, 121, 156)),
			},
			Signals.ship1Repairing : {
				(75, 238) : ((255, 239, 181), ),
				(85, 240) : ((255, 239, 181), ),
			},
			Signals.ship2Repairing : {
				(157, 238) : ((247, 227, 173), ),
				(166, 240) : ((247, 239, 181), ),
			},
			Signals.ship3Repairing : {
				(239, 238) : ((247, 227, 173), ),
				(248, 240) : ((247, 239, 181), ),
			},
			Signals.ship4Repairing : {
				(320, 238) : ((247, 223, 173), ),
				(329, 240) : ((247, 239, 181), ),
			},
			Signals.ship5Repairing : {
				(401, 238) : ((255, 239, 181), ),
				(411, 240) : ((255, 243, 181), ),
			},
			Signals.ship6Repairing : {
				(483, 238) : ((247, 223, 165), ),
				(492, 240) : ((247, 239, 181), ),
			},
			Signals.ship1NeedSupply : {
				(102, 334) : ((156, 162, 156), ),
			},
			Signals.ship2NeedSupply : {
				(186, 334) : ((156, 162, 156), ),
			},
			Signals.ship3NeedSupply : {
				(267, 334) : ((156, 162, 156), ),
			},
			Signals.ship4NeedSupply : {
				(348, 336) : ((156, 162, 156), ),
			},
			Signals.ship5NeedSupply : {
				(429, 335) : ((156, 162, 156), ),
			},
			Signals.ship6NeedSupply : {
				(512, 334) : ((156, 162, 156), ),
			},
			Signals.squardon4Selected: {
				(321, 142) : ((16, 134, 231), ),
			},
			Signals.squardon3Selected: {
				(237, 142) : ((16, 134, 231), ),
			},
			Signals.squardon2Selected: {
				(150, 142) : ((16, 134, 231), ),
			},
			Signals.squardon1Selected: {
				(63, 142) : ((16, 134, 231), ),
			},
		})
		self.transition.update({
			Transitions.selectStatistic : (
				{StateKey.combatPreparationStatistic, }, 
				(123, 387, 2)
			),
			Transitions.selectQuickSupply : (
				{StateKey.combatPreparationQuickSupply, }, 
				(217, 386, 2)
			),
			Transitions.selectQuickRepair : (
				{StateKey.combatPreparationQuickRepair, }, 
				(310, 387, 2)
			),
			Transitions.backAtCombatPreparation : ({
				StateKey.sailingOffCombat,
				StateKey.sailingOffCampaign,
				StateKey.sailingOffExercise
			}, (20, 58, 2)),
			Transitions.startBattleAtCombatPreparation : ({
				StateKey.enemyInfo,
				StateKey.selectFormation,
				StateKey.chaseOrGiveUp,
				StateKey.battleResult,
			}, (611, 480, 3)),
		})
		self.behavior.update({
			Behaviors.selectSquardon1 : (76, 142, 2),
			Behaviors.selectSquardon2 : (161, 142, 2),
			Behaviors.selectSquardon3 : (248, 142, 2),
			Behaviors.selectSquardon4 : (333, 142, 2),
		})

	def getDamagedShips(self):
		damagedShips = []
		for i in range(6):
			if not self.signal[Signals(i)] and not self.signal[Signals(i+12)]:
				damagedShips.append(i+1)
			if self.signal[Signals(i+41)]:
				damagedShips.append(i+1)
		return damagedShips

	def existsShipNeedSupply(self):
		for i in range(6):
			if not self.signal[Signals(i+12)] and self.signal[Signals(i+18)]:
				return True
		return False
