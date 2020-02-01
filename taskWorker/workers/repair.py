from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from util.logger import log, Types
from state.stateKey import StateKey
from state.transitions import Transitions
from state.behaviors import Behaviors

class Repair(TaskWorker):
    def work(self, status, argument):
        damagedShips = status
        if damagedShips:
            message = self.messages.existsDamagedShipsWarning(damagedShips)
            log(message, Types.warning)
            if self.stateController.currentState.key != StateKey.combatPreparationQuickRepair:
                self.stateController.transit(Transitions.selectQuickRepair)
            for shipPos in damagedShips:
                self.stateController.behave(Behaviors(shipPos+6))
            return Status.normal
        message = self.messages.noDamagedShipsMessage()
        log(message, Types.verbose)
        return Status.final
