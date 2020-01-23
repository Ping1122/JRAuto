from mouseController import MouseController
from gameStateManager import GameStateManager
from messageService import MessageService
from logger import log, Types
from states import *
from config import *

class GameController:
    def __init__(self):
        self.gameStateManager = GameStateManager()
        self.mouseController = MouseController(self.gameStateManager)
        self.messageService = MessageService()
        self.stageBattleMap = {
            "7-1a": self.battleStage71a,
            "7-4b": self.battleStage74b
        }

    def selectStage(self, stage):
        message = self.messageService.startSelectStateMessage(
            stage,
            self.gameStateManager.currentState
        )
        log(message, Types.verbose)
        description = "select stage " + stage
        self.gameStateManager.assertCurrentStates(
            {States.sailingOffCombat},
            description
        )
        self.mouseController.clickAndWaitUntilStateChange(
            SELECT_STAGE_CLICK_POSITION,
            SELECT_STAGE_CLICK_STD,
            {States.sailingOffCombat},
            combatPreparationStates,
            False
        )

    def inspectRepairReplace(self):
        message = self.messageService.inspectRepairReplaceMessage(
            self.gameStateManager.currentState
        )
        log(message, Types.verbose)
        description = "inspect, repair and replace damaged ships"
        self.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        damagedShips = self.gameStateManager.findDamagedShips()
        if damagedShips:
            message = self.messageService.existsDamagedShipsWarning(damagedShips)
            log(message, Types.warning)
            exit(0)
        message = self.messageService.noDamagedShipsMessage()
        log(message, Types.verbose)

    def supply(self):
        message = self.messageService.startSupplyMessage(
            self.gameStateManager.currentState
        )
        log(message, Types.verbose)
        description = "quick supply ships"
        self.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        if self.gameStateManager.currentState not in combatPreparationQuickSupplyStates:
            self.mouseController.clickAndWaitUntilStateChange(
                SELECT_QUICK_SUPPLY_POSITION,
                SELECT_QUICK_SUPPLY_STD,
                combatPreparationStatisticStates | combatPreparationQuickRepairStates,
                combatPreparationQuickSupplyStates,
                False
            )
        self.mouseController.clickAndNoStageChange(
            PERFORM_QUICK_SUPPLY_POSITION,
            PERFORM_QUICK_SUPPLY_STD
        )

    def battle(self, stage):
        message = self.messageService.startBattleMessage(
            stage,
            self.gameStateManager.currentState
        )
        log(message, Types.verbose)
        self.stageBattleMap[stage]()

    def battleStage71a(self):
        description = "battle 7-1a"
        self.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        self.startCombatAtCombatPreparation()
        self.startCombatAtEnemyInfo()
        self.selectFormation(SELECT_SINGLE_HORIZONTAL_POSITION,SELECT_SINGLE_HORIZONTAL_STD)
        if self.gameStateManager.currentState == States.nightBattleOrGiveUp:
            self.giveUpAtNightBattleOrGiveUp()
        self.retreatAtForwardOrRetreat()


    def battleStage74b(self):
        description = "battle 7-4b"
        self.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        self.startCombatAtCombatPreparation()
        if self.gameStateManager.checkStage74bExistsSubmarine():
            message = self.messageService.stage74bExistsSubmarineMessage()
            log(message, Types.verbose)
            self.retreatAtEnemyInfo()
            return
        self.startCombatAtEnemyInfo()
        self.selectFormation(SELECT_SINGLE_VERTICAL_POSITION,SELECT_SINGLE_VERTICAL_STD)
        if self.gameStateManager.currentState == States.nightBattleOrGiveUp:
            self.giveUpAtNightBattleOrGiveUp()
        self.retreatAtForwardOrRetreat()

    def startCombatAtCombatPreparation(self):
        self.mouseController.clickAndWaitUntilStateChange(
            START_COMBAT_POSITION,
            START_COMBAT_STD,
            combatPreparationStates,
            {States.enemyInfo},
            True
        )

    def retreatAtEnemyInfo(self):
        self.mouseController.clickAndWaitUntilStateChange(
            RETREAT_ENEMY_INFO_POSITION,
            RETREAT_ENEMY_INFO_STD,
            {States.enemyInfo},
            {States.sailingOffCombat},
            False
        )

    def startCombatAtEnemyInfo(self):
        self.mouseController.clickAndWaitUntilStateChange(
            START_BATTLE_ENEMY_INFO_POSITION,
            START_BATTLE_ENEMY_INFO_STD,
            {States.enemyInfo},
            {States.selectFormation},
            False
        )

    def selectFormation(self, position, std):
        self.mouseController.clickAndWaitUntilStateChange(
            position,
            std,
            {States.selectFormation},
            {States.nightBattleOrGiveUp, States.forwardOrRetreat},
            True
        )

    def giveUpAtNightBattleOrGiveUp(self):
        self.mouseController.clickAndWaitUntilStateChange(
            RETREAT_FORWARD_OR_RETREAT_POSITION,
            RETREAT_FORWARD_OR_RETREAT_STD,
            {States.nightBattleOrGiveUp},
            {States.forwardOrRetreat},
            True
        )

    def retreatAtForwardOrRetreat(self):
        self.mouseController.clickAndWaitUntilStateChange(
            RETREAT_FORWARD_OR_RETREAT_POSITION,
            RETREAT_FORWARD_OR_RETREAT_STD,
            {States.forwardOrRetreat},
            {States.sailingOffCombat},
            False
        )
