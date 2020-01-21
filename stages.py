from actions import *
from logger import *

def startStage74():
	initialize()
	while True:
		selectStage("7-4")
		damagedShips = inspectRepairReplace()
		if damagedShips:
			message = "Ship " + str(damagedShips) + "are damaged, stop auto play"
			log(message, Type.warning)
			break	
		supply()
		battle()

stages = {
	"7-4": startStage74,
}