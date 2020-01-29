from controllers.stateController import StateController
from controllers.mouseController import MouseController
from state.transitions import Transitions
from state.behaviors import Behaviors
from state.signals import Signals
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

    def collectAndRestartExpidition(self):
        while self.stateController.currentState.signal[Signals.existsCompletedExpidition]:
            message = self.messages.existsCompletedExpiditionMessage()
            log(message, Types.verbose)
            if self.stateController.currentState.key != StateKey.sailingOffExpidition:
                self.stateController.transit(Transitions.selectExpidition)
            for i in range(4):
                if self.stateController.currentState.signal[Signals(i+8)]:
                    self.stateController.transit(Transitions(i+29))
                    self.stateController.transit(Transitions.confirmAtContinueExpidition)
            self.stateController.transit(Transitions.selectCombat)

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
            if self.stateController.currentState.key != StateKey.combatPreparationQuickRepair:
                self.stateController.transit(Transitions.selectQuickRepair)
            for shipPos in damagedShips:
                self.stateController.behave(Behaviors(shipPos+6))
            self.stateController.updateState()
            self.inspectRepairReplace()
            return
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
        if self.stateController.currentState.key == StateKey.newShip:
            self.stateController.transit(Transitions.confirmAtNewShip)
        if self.stateController.currentState.key == StateKey.flagshipSeriousDamaged:
            self.stateController.transit(Transitions.retreatAtFlagshipSeriousDamage)
            self.stateController.transit(Transitions.sailingOff)
            if self.stateController.currentState.key == StateKey.sailingOffExpidition:
                self.stateController.transit(Transitions.selectCombat)
            return
        self.stateController.transit(Transitions.retreatAtForwardOrRetreat)

    def battleStage74b(self):
        self.stateController.transit(Transitions.startBattleAtCombatPreparation)
        if self.stateController.currentState.signal[Signals.stage74bExistsSubmarine]:
            message = self.messages.stage74bExistsSubmarineMessage()
            log(message, Types.verbose)
            self.stateController.transit(Transitions.retreatAtEnemyInfo)
            return
        self.stateController.transit(Transitions.startBattleAtEnemyInfo)
        self.stateController.transit(Transitions.selectSingleVertical)
        if self.stateController.currentState.key == StateKey.chaseOrGiveUp:
            self.stateController.transit(Transitions.giveUp)
        if self.stateController.currentState.key == StateKey.newShip:
            self.stateController.transit(Transitions.confirmAtNewShip)
        if self.stateController.currentState.key == StateKey.flagshipSeriousDamaged:
            self.stateController.transit(Transitions.retreatAtFlagshipSeriousDamage)
            self.stateController.transit(Transitions.sailingOff)
            if self.stateController.currentState.key == StateKey.sailingOffExpidition:
                self.stateController.transit(Transitions.selectCombat)
            return
        self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
