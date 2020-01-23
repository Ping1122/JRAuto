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
	print(currentState)

def selectStage(stage):
	assertCurrentState(States.sailingOffCombat, "select stage")
	while currentState == States.sailingOffCombat:
		simulateSingleClick(SELECT_STAGE_CLICK_POSITION, SELECT_STAGE_CLICK_STD)
		time.sleep(2)
		updateScreenshotAndState()

def inspectRepairReplace():
	description = "inspect, repair and replace damaged ships"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	damagedShips = findDamagedShips(currentScreenshot)
	if damagedShips:
		message = "Ship " + str(damagedShips) + "are damaged, stop auto play"
		log(message, Types.warning)
		exit(0)

def supply():
	description = "quick supply ships"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	if not isCombatPreparationQuickSupplyState(currentState):
		simulateSingleClick(SELECT_QUICK_SUPPLY_POSITION, SELECT_QUICK_SUPPLY_STD)
		updateScreenshotAndState()
	assertCurrentStateSatisfyCondition(isCombatPreparationQuickSupplyState, description)
	simulateSingleClick(PERFORM_QUICK_SUPPLY_POSITION, PERFORM_QUICK_SUPPLY_STD)
	time.sleep(2)

def battle74b():
	description = "battle 7-4b"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	simulateSingleClick(START_COMBAT_POSITION, START_COMBAT_STD)
	time.sleep(1)
	waitForState(States.enemyInfo)
	assertCurrentState(States.enemyInfo, description)
	if checkStage74bExistsSubmarine(currentScreenshot):
		simulateSingleClick(RETREAT_ENEMY_INFO_POSITION, RETREAT_ENEMY_INFO_STD)
		time.sleep(2)
		updateScreenshotAndState()
		return
	simulateSingleClick(START_BATTLE_ENEMY_INFO_POSITION, START_BATTLE_ENEMY_INFO_STD)
	updateScreenshotAndState()
	assertCurrentState(States.selectFormation, description)
	simulateSingleClick(SELECT_SINGLE_VERTICAL_POSITION, SELECT_SINGLE_VERTICAL_STD)
	waitForStates({States.nightBattleOrGiveUp, States.forwardOrRetreat})
	if currentState == States.nightBattleOrGiveUp:
		simulateSingleClick(RETREAT_FORWARD_OR_RETREAT_POSITION, RETREAT_FORWARD_OR_RETREAT_STD)
		waitForState(States.forwardOrRetreat)
	simulateSingleClick(RETREAT_FORWARD_OR_RETREAT_POSITION, RETREAT_FORWARD_OR_RETREAT_STD)
	time.sleep(2)
	updateScreenshotAndState()

def battle71a():
	description = "battle 7-1a"
	assertCurrentStateSatisfyCondition(isCombatPreparationState, description)
	simulateSingleClick(START_COMBAT_POSITION, START_COMBAT_STD)
	time.sleep(1)
	waitForState(States.enemyInfo)
	assertCurrentState(States.enemyInfo, description)
	simulateSingleClick(START_BATTLE_ENEMY_INFO_POSITION, START_BATTLE_ENEMY_INFO_STD)
	updateScreenshotAndState()
	assertCurrentState(States.selectFormation, description)
	simulateSingleClick(SELECT_SINGLE_HORIZONTAL_POSITION , SELECT_SINGLE_HORIZONTAL_STD)
	waitForStates({States.nightBattleOrGiveUp, States.forwardOrRetreat})
	if currentState == States.nightBattleOrGiveUp:
		simulateSingleClick(RETREAT_FORWARD_OR_RETREAT_POSITION, RETREAT_FORWARD_OR_RETREAT_STD)
		waitForState(States.forwardOrRetreat)
	simulateSingleClick(RETREAT_FORWARD_OR_RETREAT_POSITION, RETREAT_FORWARD_OR_RETREAT_STD)
	time.sleep(2)
	updateScreenshotAndState()



def battle(stage):
	if stage == "7-4b":
		battle74b()
	elif stage == "7-1a":
		battle71a()

def waitForState(state):
	description = "wait for " + str(state)
	time.sleep(1)
	updateScreenshotAndState()
	iterationCount = 0
	while currentState != state:
		assertCurrentState(States.unknown, description)
		simulateShortClick(SAILING_OFF_ENEMY_INFO_POSITION, SAILING_OFF_ENEMY_INFO_STD)
		iterationCount += 1
		if iterationCount % 5 == 0:
			updateScreenshotAndState()

def waitForStates(states):
	description = "wait for " + str(states)
	time.sleep(1)
	updateScreenshotAndState()
	iterationCount = 0
	while currentState not in states:
		assertCurrentState(States.unknown, description)
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
	if not stateCondition(currentState):
		message = "Trying to " + description + ", but not in the valid states."
		log(message, Types.error)
		exit(1)

