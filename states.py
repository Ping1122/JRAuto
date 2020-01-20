from enum import Enum     

States = Enum(
	'States', 
	'unknown ' + 
	'gameClose ' +
	'login ' +
	'home ' +
	'sailingOffCombat ' +
	'sailingOffExpidition ' +
	'combatPreparationStatisticSquadron1 ' 
)

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
	(1451, 580) : (16, 36, 60, 255),
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

squadron1Signature = {
	# Assumption: squadrom1 selected style does not change
	(123, 127) : (16, 132, 228, 255),
	(147, 126) : (247, 251, 254, 255),
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
	}

}

