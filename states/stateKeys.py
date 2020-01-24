from util.orderedEnum import OrderedEnum

class StateKeys(OrderedEnum):
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
	flagshipSeriousDamaged = 21
	forwardOrRetreat = 22