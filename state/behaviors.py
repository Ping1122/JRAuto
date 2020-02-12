from enum import IntEnum

class Behaviors(IntEnum):
	repairAllShips = 0
	supplyAllShips = 1,
	selectSquardon1 = 2,
	selectSquardon2 = 3,
	selectSquardon3 = 4,
	selectSquardon4 = 5,
	checkNoNewsToday = 6,
	repairShip1 = 7,
	repairShip2 = 8,
	repairShip3 = 9,
	repairShip4 = 10,
	repairShip5 = 11,
	repairShip6 = 12,
	switchMode = 13,
	incrementStage = 14,
	decrementStage = 15,
	nextMap = 16,
	prevMap = 17,
	switchStrategy = 18,
	confirm = 19
