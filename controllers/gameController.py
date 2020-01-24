from controllers.gameStateManager import GameStateManager
from controllers.mouseController import MouseController
from util.messages import Messages
from util.logger import log, Types
from data.constants import *
from data.states import *

class GameController:
    def __init__(self):
        self.gameStateManager = GameStateManager()
        self.mouseController = MouseController(self.gameStateManager)
        self.messages = Messages()
        self.stageBattleMap = {
            "7-1a": self.battleStage71a,
            "7-4b": self.battleStage74b
        }

    def selectStage(self, stage):
        message = self.messages.startSelectStateMessage(
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
        message = self.messages.inspectRepairReplaceMessage(
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
            message = self.messages.existsDamagedShipsWarning(damagedShips)
            log(message, Types.warning)
            exit(0)
        message = self.messages.noDamagedShipsMessage()
        log(message, Types.verbose)

    def supply(self):
        message = self.messages.startSupplyMessage(
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
        message = self.messages.startBattleMessage(
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
        if self.gameStateManager.currentState == States.flagshipSeriousDamaged:
            self.retreatAtFlagshipSeriousDamage()
            self.startSailingOff()
            if self.gemeStateManager.currentState == States.sailingOffExpidition:
                self.selectCombat()
            return
        self.retreatAtForwardOrRetreat()

    def battleStage74b(self):
        description = "battle 7-4b"
        self.gameStateManager.assertCurrentStates(
            combatPreparationStates,
            description
        )
        self.startCombatAtCombatPreparation()
        if self.gameStateManager.checkStage74bExistsSubmarine():
            message = self.messages.stage74bExistsSubmarineMessage()
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
            {
                States.nightBattleOrGiveUp,
                States.flagshipSeriousDamaged,
                States.forwardOrRetreat,
            },
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

    def retreatAtFlagshipSeriousDamaged(self):
        self.mouseController.clickAndWaitUntilStateChange(
            FALGSHIP_SERIOUS_DAMAGED_RETREAT_POSITION,
            FALGSHIP_SERIOUS_DAMAGED_RETREAT_STD,
            {States.flagshipSeriousDamaged},
            {States.home},
            False
        )

    def startSailingOff(self):
        self.mouseController.clickAndWaitUntilStateChange(
            (1405, 765),
            7,
            {States.home},
            {States.sailingOffCombat, sailingOffExpidition},
            False
        )

    def selectCombat(self):
        self.mouseController.clickAndWaitUntilStateChange(
            (267, 37),
            3,
            {States.sailingOffExpidition},
            {States.sailingOffCombat},
            False
        )

    def retreatAtForwardOrRetreat(self):
        self.mouseController.clickAndWaitUntilStateChange(
            RETREAT_FORWARD_OR_RETREAT_POSITION,
            RETREAT_FORWARD_OR_RETREAT_STD,
            {States.forwardOrRetreat},
            {States.sailingOffCombat},
            False
        )
