from appscript import *
from config import *
import time
from monitor import *
from mouse import *
from states import *
from logger import *

currentScreenshot = None
currentState = None
updateScreenshotAndState()

def updateScreenshotAndState():
	global currentScreenshot
	global currentState
	currentScreenshot = takeScreenshot()
	currentState = analyzeState(currentScreenshot)

def inspectRepairReplace():
	description = "inspect, repair and replace damaged ships"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	damagedShips = findDamagedShips(currentScreenshot)
	if damagedShips:
		message = "Ship " + str(damagedShips) + "are damaged, stop auto play"
		log(message, Type.warning)
		exit(0)

def selectStage(stage):
	assertCurrentState(States.sailingOffCombat, "select stage")
	singleClick(SELECT_STAGE_CLICK_POSITION, SELECT_STAGE_CLICK_STD)
	updateScreenshotAndState()

def supply():
	description = "quick supply ships"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	singleClick(SELECT_STAGE_CLICK_POSITION, SELECT_STAGE_CLICK_STD)
	updateScreenshotAndState()
	

def battle():
	pass

def openSimulator():
	simulator = app("/Applications/NemuPlayer.app")
	simulator.run()
	isOpen = False;
	while not isOpen:
		time.sleep(START_SIMULATOR_RETRY_TIME)

def assertCurrentState(state, description):
	if currentState != state:
		message = "Trying to " + description + ", but not in "+ str(state) + " screen."
		log(message, Types.error)
		exit(1)
		
def assertCurrentStateSatisfyCondition(stateCondition, description):
	print(currentScreenshot)
	if not stateCondition(currentState):
		message = "Trying to " + description + ", but not in the valid states."
		log(message, Types.error)
		exit(1)

initialize()
print(inspectRepairReplace())