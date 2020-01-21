from appscript import *
from config import *
import time
from monitor import *
from mouse import *
from states import *
from logger import *

currentScreenshot = None
currentState = None

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
	simulateSingleClick(SELECT_STAGE_CLICK_POSITION, SELECT_STAGE_CLICK_STD)
	updateScreenshotAndState()

def supply():
	description = "quick supply ships"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	if not isCombatPreparationQuickSupplyState(currentState):
		simulateSingleClick(SELECT_QUICK_SUPPLY_POSITION, SELECT_QUICK_SUPPLY_STD)
		updateScreenshotAndState()
	assertCurrentStateSatisfyCondition(isCombatPreparationQuickSupplyState, description)
	simulateSingleClick(PERFORM_QUICK_SUPPLY_POSITION, PERFORM_QUICK_SUPPLY_STD)
	time.sleep(2)

def battle():
	description = "battle"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	simulateSingleClick(START_COMBAT_POSITION, START_COMBAT_STD)
	waitForState(States.enemyInfo)
	assertCurrentState(States.enemyInfo, description)
	if checkStage74bExistsSubmarine():
		simulateSingleClick(RETREAT_ENEMY_INFO_POSITION, RETREAT_ENEMY_INFO_STD)
		time.sleep(2)
		return
	simulateSingleClick(START_BATTLE_ENEMY_INFO_POSITION, START_BATTLE_ENEMY_INFO_STD)




def waitForState(state):
	iterationCount = 0
	while currentState != state:
		simulateShortClick(SAILING_OFF_ENEMY_INFO_POSITION, SAILING_OFF_ENEMY_INFO_STD)
		iterationCount += 1
		if iterationCount % 5 == 0:
			updateScreenshotAndState()

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

updateScreenshotAndState()