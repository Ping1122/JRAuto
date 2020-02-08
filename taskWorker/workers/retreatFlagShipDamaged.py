from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from state.stateKey import StateKey
from util.logger import log, Types

class RetreatFlagShipDamaged(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.flagShipSeriousDamaged:
            return status
        message = self.messages.retreatFlagShipDamaged()
        log(message, Types.verbose)
        self.stateController.transit(Transitions.retreatAtFlagShipSeriousDamaged)
        self.stateController.transit(Transitions.sailingOff)
        if self.stateController.currentState.key == StateKey.sailingOffExpidition:
            self.stateController.transit(Transitions.selectCombat)
        return Status.normal
