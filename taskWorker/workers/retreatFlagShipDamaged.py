from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions

class RetreatFlagShipDamaged(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key == StateKey.flagShipSeriousDamaged:
            self.stateController.transit(Transitions.retreatAtFlagshipSeriousDamage)
            self.stateController.transit(Transitions.sailingOff)
            if self.stateController.currentState.key == StateKey.sailingOffExpidition:
                self.stateController.transit(Transitions.selectCombat)
            return Status.final
        return status
