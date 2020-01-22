from mouseController import MouseController
from gameStateManager import GameStateManager
from states import *
from config import *

class GameController:
    def __init__:
        this.gameStateManager = GameStateManager()
        this.mouseController = MouseController(this.gameStateManager)
        this.stageBattleMap = {
            "7-1a": battleStage71a,
            "7-4b": battleStage74b
        }

    def selectStage(stage):
        description = "select stage " + stage
    	this.gameStateManager.assertCurrentStates(
            {States.sailingOffCombat},
            description
        )
        this.mouseController.clickAndWaitUntilStateChange(
            SELECT_STAGE_CLICK_POSITION,
            SELECT_STAGE_CLICK_STD,
            {States.sailingOffCombat},
            combatPreparationStates,
            False
        )

    def inspectRepairReplace():
    	description = "inspect, repair and replace damaged ships"
        this.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        damagedShips = this.gameStateManager.findDamagedShips(currentScreenshot)
        if damagedShips:
            message = "Ship " + str(damagedShips) + " are damaged, stop auto play"
    		log(message, Types.warning)
    		exit(0)

    def supply():
    	description = "quick supply ships"
        this.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        if this.gameStateManager.currentState not in combatPreparationStates:
            this.mouseController.clickAndWaitUntilStateChange(
                SELECT_QUICK_SUPPLY_POSITION,
                SELECT_QUICK_SUPPLY_STD,
                {
                    **combatPreparationStatisticStates,
                    **combatPreparationQuickSupplyStates
                },
                combatPreparationQuickRepairStates,
                False
            )
        this.mouseController.clickAndNoStageChange(
            PERFORM_QUICK_SUPPLY_POSITION,
            PERFORM_QUICK_SUPPLY_STD
        )

    def battle(stage):
        this.stageBattleMap[stage]()

    def battleStage71a():
        description = "battle 7-1a"
        this.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        this.startCombatAtCombatPreparation()
        this.startCombatAtEnemyInfo()
        this.selectFormation(SELECT_SINGLE_HORIZONTAL_POSITION,SELECT_SINGLE_HORIZONTAL_STD)
        if this.gameStateManager.currentState == States.nightBattleOrGiveUp:
            this.giveUpAtNightBattleOrGiveUp()
        this.retreatAtForwardOrRetreat()


    def battleStage74b():
        description = "battle 7-4b"
        this.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        this.startCombatAtCombatPreparation()
        if this.gameStateManager.checkStage74bExistsSubmarine():
            this.retreatAtEnemyInfo()
            return
        this.startCombatAtEnemyInfo()
        this.selectFormation(SELECT_SINGLE_VERTICAL_POSITION,SELECT_SINGLE_VERTICAL_STD)
        if this.gameStateManager.currentState == States.nightBattleOrGiveUp:
            this.giveUpAtNightBattleOrGiveUp()
        this.retreatAtForwardOrRetreat()

    def startCombatAtCombatPreparation():
        this.mouseController.clickAndWaitUntilStateChange(
            START_COMBAT_POSITION,
            START_COMBAT_STD,
            combatPreparationStates,
            {States.enemyInfo},
            True
        )

    def retreatAtEnemyInfo():
        this.mouseController.clickAndWaitUntilStateChange(
            RETREAT_ENEMY_INFO_POSITION,
            RETREAT_ENEMY_INFO_STD,
            {States.enemyInfo},
            {States.sailingOffCombat},
            False
        )

    def startCombatAtEnemyInfo():
        this.mouseController.clickAndWaitUntilStateChange(
            START_BATTLE_ENEMY_INFO_POSITION,
            START_BATTLE_ENEMY_INFO_STD,
            {States.enemyInfo},
            {States.selectFormation},
            False
        )

    def selectFormation(position, std):
        this.mouseController.clickAndWaitUntilStateChange(
            position,
            std,
            {States.selectFormation},
            {States.nightBattleOrGiveUp, States.forwardOrRetreat},
            True
        )

    def giveUpAtNightBattleOrGiveUp():
        this.mouseController.clickAndWaitUntilStateChange(
            RETREAT_FORWARD_OR_RETREAT_POSITION,
            RETREAT_FORWARD_OR_RETREAT_STD,
            {States.nightBattleOrGiveUp},
            {States.forwardOrRetreat}.
            False
        )

    def retreatAtForwardOrRetreat():
        this.mouseController.clickAndWaitUntilStateChange(
            RETREAT_FORWARD_OR_RETREAT_POSITION,
            RETREAT_FORWARD_OR_RETREAT_STD,
            {States.forwardOrRetreat},
            {States.sailingOffCombat},
            False
        )
