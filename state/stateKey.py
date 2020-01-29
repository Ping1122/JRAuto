from enum import IntEnum

class StateKey(IntEnum):
	unknown = 0
	attendence = 1,
	chaseOrGiveUp = 2,
	combatPreparationQuickRepair = 3,
	combatPreparationQuickSupply = 4,
	combatPreparationStatistic = 5,
	enemyInfo = 6,
	forwardOrRetreat = 7,
	gameClosed = 8,
	home = 9,
	login = 10,
	newsAndAnnouncement = 11,
	obtainLoginResource = 12,
	sailingOffCampaign = 13,
	sailingOffCombat = 14,
	sailingOffExercise = 15,
	sailingOffExpidition = 16,
	selectFormation = 17,
	continueExpidition = 18,
	newShip = 19,
	flagShipSeriousDamaged = 20

