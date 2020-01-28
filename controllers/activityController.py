from controllers.stateController import StateController
from controllers.mouseController import MouseController
from state.transitions import Transitions
from state.behaviors import Behaviors
from state.stateKey import StateKey
from util.messages import Messages
from util.logger import log, Types
from data.constants import *

class ActivityController:
    def __init__(self):
        self.stateController = StateController()
        self.messages = Messages()
        self.stageBattleMap = {
            "7-1a": self.battleStage71a,
            "7-4b": self.battleStage74b
        }

    def selectStage(self, stage):
        message = self.messages.startSelectStateMessage(stage, self.stateController.currentState.key)
        log(message, Types.verbose)
        self.stateController.transit(Transitions.selectStage)

    def inspectRepairReplace(self):
        message = self.messages.inspectRepairReplaceMessage(self.stateController.currentState.key)
        log(message, Types.verbose)
        damagedShips = self.stateController.currentState.getDamagedShips()
        if damagedShips:
            message = self.messages.existsDamagedShipsWarning(damagedShips)
            log(message, Types.warning)
            exit(0)
        message = self.messages.noDamagedShipsMessage()
        log(message, Types.verbose)

    def supply(self):
        message = self.messages.startSupplyMessage(self.stateController.currentState.key)
        log(message, Types.verbose)
        if self.stateController.currentState.key !=  StateKey.combatPreparationQuickSupply:
            self.stateController.transit(Transitions.selectQuickSupply)
        self.stateController.behave(Behaviors.supplyAllShips)

    def battle(self, stage):
        message = self.messages.startBattleMessage(stage, self.stateController.currentState.key)
        log(message, Types.verbose)
        self.stageBattleMap[stage]()

    def battleStage71a(self):
        self.stateController.transit(Transitions.startBattleAtCombatPreparation)
        self.stateController.transit(Transitions.startBattleAtEnemyInfo)
        self.stateController.transit(Transitions.selectSingleHorizontal)
        if self.stateController.currentState.key == StateKey.chaseOrGiveUp:
            self.stateController.transit(Transitions.giveUp)
        self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
        # if self.stateController.currentState == States.flagshipSeriousDamaged:
        #     self.retreatAtFlagshipSeriousDamage()
        #     self.startSailingOff()
        #     if self.gemeStateController.currentState == States.sailingOffExpidition:
        #         self.selectCombat()
        #     return

    def battleStage74b(self):
        self.stateController.transit(Transitions.startBattleAtCombatPreparation)
        if self.stateController.currentState.signals.stage74bExistSubmarine:
            message = self.messages.stage74bExistsSubmarineMessage()
            log(message, Types.verbose)
            self.stateController.transit(Transitions.retreatAtEnemyInfo)
            return
        self.stateController.transit(Transitions.startBattleAtEnemyInfo)
        self.stateController.transit(Transitions.selectSingleVertical)
        if self.stateController.currentState.key == StateKey.chaseOrGiveUp:
            self.stateController.transit(Transitions.giveUp)
        self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
        # TODO: handle flag ship damaged
