from util.orderedEnum import OrderedEnum

class Transitions(OrderedEnum):
	confirm = 0
	chase = 1,
	giveUp = 2,
	selectStatistic = 3,
	selectQuickSupply = 4,
	selectQuickRepair = 5,
	backAtCombatPreparation = 6,
	startBattleAtCombatPreparation = 7,
	retreatAtEnemyInfo = 8,
	startBattleAtEnemyInfo = 9,
	forward = 10,
	retreatAtForwardOrRetreat = 11,
	startGame = 12,
	sailingOff = 13,
	selectStage = 14,
	selectSingleVertical = 15,
	selectDoubleVertical = 16,
	selectWheelShape = 17,
	selectTrapezoidShape = 18,
	selectSingleHorizontal = 19,
	close = 20,
	obtainResource = 21,
	backAtSailingOff = 22,
	selectCombat = 23,
	selectCampaign = 24,
	selectExercise = 25,
	selectExpidition = 26




