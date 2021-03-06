from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from util.logger import log, Types
from state.stateKey import StateKey
from state.transitions import Transitions
from state.behaviors import Behaviors

class Repair(TaskWorker):
    def workCombat(self, status):
        return self.repairDamagedShips(status)

    def workCampaign(self, status):
        self.repairDamagedShips(status[0])
        return status[1]

    def workExercise(self, status):
        self.repairDamagedShips(status[0])
        return status[1]

    def repairDamagedShips(self, damagedShips):
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
        return Status.normal
