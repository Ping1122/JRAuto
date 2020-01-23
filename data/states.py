from ..util.orderedEnum import OrderedEnum

class States(OrderedEnum):
	unknown = 0
	gameClose = 1
	login = 2
	home = 3
	sailingOffCombat = 4
	sailingOffExpidition = 5
	combatPreparationStatisticSquadron1 = 6
	combatPreparationStatisticSquadron2 = 7
	combatPreparationStatisticSquadron3 = 8
	combatPreparationStatisticSquadron4 = 9
	combatPreparationQuickSupplySquadron1 = 10
	combatPreparationQuickSupplySquadron2 = 11
	combatPreparationQuickSupplySquadron3 = 12
	combatPreparationQuickSupplySquadron4 = 13
	combatPreparationQuickRepairSquadron1 = 14
	combatPreparationQuickRepairSquadron2 = 15
	combatPreparationQuickRepairSquadron3 = 16
	combatPreparationQuickRepairSquadron4 = 17
	enemyInfo = 18
	selectFormation = 19
	nightBattleOrGiveUp = 20
	forwardOrRetreat = 21
	attendence = 22

gameCloseSignature = {
	# Assumption: background does not change
	(98, 188) : (31, 33, 41, 255),
	(634, 178) : (36, 39, 48, 255),
	(1356, 186) : (29, 31, 40, 255),
	(214, 552) : (33, 35, 44, 255),
	(730, 534) : (34, 37, 48, 255),
	(1426, 576) : (32, 35, 43, 255)
}

loginSignature = {
	# Assumption: account management tag does not change
	(72, 704) : (56, 56, 56, 255),
	(144, 701) : (187, 187, 187, 255),
	(40, 695) : (183, 197, 201, 255),
	(134, 683) : (237, 237, 237, 255),
	(102, 730) : (237, 237, 237, 255),
	(180, 727) : (237, 237, 237, 255),
}

homeSignature = {
	# Assumption: the logo does not change
	(1404, 760) : (140, 149, 153, 255),
	(1170, 744) : (255, 145, 118, 255),
	(986, 751) : (54, 129, 201, 255),
	(73, 743) : (255, 255, 255, 255),
	(1388, 668) : (67, 67, 67, 255),
	(73, 797) : (0, 160, 233, 255),
}

sailingOffSignature = {
	# Assumption: background left-top logo does not change
	(1453, 36) : (14, 17, 32, 255),
	(1219, 74) : (55, 68, 88, 255),
	(1326, 780) : (88, 100, 117, 255),
	(49, 778) : (67, 77, 88, 255),
	(1479, 409) : (17, 38, 59, 255),
	(44, 14) : (84, 86, 96, 255),
}

combatSignature = {
	# Assumption: combat selected style does not change
	(248, 32) : (254, 255, 255, 255),
	(200, 30) : (16, 132, 228, 255),
}

expiditionSignature = {
	# Assumption: expodition selected style does not change
	(585, 46) : (16, 132, 229, 255),
	(633, 49) : (254, 255, 255, 255),
}

combatPreparationSignature = {
	# Assumption: top-left logo and right-bottom logo does not change
	(78, 44) : (192, 193, 197, 255),
	(142, 36) : (255, 255, 255, 255),
	(250, 53) : (202, 205, 210, 255),
	(99, 666) : (36, 52, 73, 255),
	(1198, 780) : (255, 218, 47, 255),
	(1352, 780) : (35, 35, 34, 255),
}

statisticSignature = {
	# Assumption: statistic selected style does not change
	(182, 668) : (30, 139, 240, 255),
	(219, 666) : (251, 254, 255, 255),
}

quickSupplySignature = {
	# Assumption: supply selected style does not change
	(369, 669) : (30, 138, 240, 255),
	(417, 665) : (254, 255, 255, 255),
}

quickRepairSignature = {
	# Assumption: repair selected style does not change
	(383, 658) : (34, 68, 95, 255),
	(449, 651) : (230, 235, 238, 255),
}

squadron1Signature = {
	# Assumption: squadrom1 selected style does not change
	(123, 127) : (16, 132, 228, 255),
	(147, 126) : (247, 251, 254, 255),
}

squadron2Signature = {
	# Assumption: squadrom2 selected style does not change
	(314, 136) : (16, 132, 229, 255),
	(326, 126) : (206, 230, 249, 255),
}

squadron3Signature = {
	# Assumption: squadrom3 selected style does not change
	(502, 137) : (15, 132, 229, 255),
	(512, 127) : (250, 252, 255, 255),
}

squadron4Signature = {
	# Assumption: squadrom4 selected style does not change
	(659, 130) : (16, 132, 228, 255),
	(705, 139) : (255, 255, 255, 255),
}

enemyInfoSignature = {
	# Assumption: right-bottom logo does not change
	(1018, 754) : (119, 12, 13, 255),
	(1074, 768) : (240, 231, 231, 255),
	(1130, 794) : (249, 245, 245, 255),
	(1231, 814) : (195, 175, 45, 255),
	(1231, 814) : (195, 175, 45, 255),
	(1291, 769) : (0, 0, 0, 255),
	(1407, 787) : (0, 0, 0, 255),
}

selectFormationSignature = {
	(864, 168) : (255, 255, 255, 255),
	(811, 486) : (255, 255, 255, 255),
	(819, 358) : (255, 255, 255, 255),
	(749, 652) : (255, 255, 255, 255),
	(718, 758) : (255, 255, 255, 255),
	(1421, 778) : (52, 52, 52, 255),
}

nightBattleOrGiveUpSignature = {
	(443, 329) : (204, 204, 204, 255),
	(444, 355) : (97, 97, 97, 255),
	(554, 553) : (152, 7, 7, 255),
	(976, 534) : (39, 149, 252, 255),
	(496, 562) : (228, 193, 193, 255),
	(973, 552) : (211, 233, 253, 255),
}

forwardOrRetreatSignature = {
	(443, 329) : (204, 204, 204, 255),
	(444, 355) : (97, 97, 97, 255),
	(554, 553) : (152, 7, 7, 255),
	(976, 534) : (39, 149, 252, 255),
	(504, 547) : (197, 109, 109, 255),
	(973, 552) : (75, 163, 246, 255),
}

attendenceSignature = {
	# TODO
}

stateSignature = {
	States.gameClose : gameCloseSignature,
	States.login : loginSignature,
	States.home : homeSignature,
	States.sailingOffCombat : {
		**sailingOffSignature,
		**combatSignature
	},
	States.sailingOffExpidition : {
		**sailingOffSignature,
		**expiditionSignature
	},
	States.combatPreparationStatisticSquadron1 : {
		**combatPreparationSignature,
		**statisticSignature,
		**squadron1Signature
	},
	States.combatPreparationStatisticSquadron2 : {
		**combatPreparationSignature,
		**statisticSignature,
		**squadron2Signature
	},
	States.combatPreparationStatisticSquadron3 : {
		**combatPreparationSignature,
		**statisticSignature,
		**squadron3Signature
	},
	States.combatPreparationStatisticSquadron4 : {
		**combatPreparationSignature,
		**statisticSignature,
		**squadron4Signature
	},
	States.combatPreparationQuickSupplySquadron1 : {
		**combatPreparationSignature,
		**quickSupplySignature,
		**squadron1Signature,
	},
	States.combatPreparationQuickSupplySquadron2 : {
		**combatPreparationSignature,
		**quickSupplySignature,
		**squadron2Signature,
	},
	States.combatPreparationQuickSupplySquadron3 : {
		**combatPreparationSignature,
		**quickSupplySignature,
		**squadron3Signature,
	},
	States.combatPreparationQuickSupplySquadron4 : {
		**combatPreparationSignature,
		**quickSupplySignature,
		**squadron4Signature,
	},
	States.combatPreparationQuickRepairSquadron1 : {
		**combatPreparationSignature,
		**quickRepairSignature,
		**squadron1Signature
	},
	States.combatPreparationQuickRepairSquadron2 : {
		**combatPreparationSignature,
		**quickRepairSignature,
		**squadron2Signature
	},
	States.combatPreparationQuickRepairSquadron3 : {
		**combatPreparationSignature,
		**quickRepairSignature,
		**squadron3Signature
	},
	States.combatPreparationQuickRepairSquadron4 : {
		**combatPreparationSignature,
		**quickRepairSignature,
		**squadron4Signature
	},
	States.enemyInfo: enemyInfoSignature,
	States.selectFormation : selectFormationSignature,
	States.nightBattleOrGiveUp : nightBattleOrGiveUpSignature,
	States.forwardOrRetreat : forwardOrRetreatSignature,
	#States.attendence : attendenceSignature,
}

combatPreparationStatisticStates = {
	States.combatPreparationStatisticSquadron1,
	States.combatPreparationStatisticSquadron2,
	States.combatPreparationStatisticSquadron3,
	States.combatPreparationStatisticSquadron4,
}

combatPreparationQuickSupplyStates = {
	States.combatPreparationQuickSupplySquadron1,
	States.combatPreparationQuickSupplySquadron2,
	States.combatPreparationQuickSupplySquadron3,
	States.combatPreparationQuickSupplySquadron4,
}

combatPreparationQuickRepairStates = {
	States.combatPreparationQuickRepairSquadron1,
	States.combatPreparationQuickRepairSquadron2,
	States.combatPreparationQuickRepairSquadron3,
	States.combatPreparationQuickRepairSquadron4,
}

combatPreparationStates = \
	combatPreparationStatisticStates | \
	combatPreparationQuickSupplyStates | \
	combatPreparationQuickRepairStates
