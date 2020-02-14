from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey
from state.transitions import Transitions

class CheckBattle(TaskWorker):
    def workCombat(self, status):
        if self.stateController.currentState.key == StateKey.home:
            self.stateController.transit(Transitions.sailingOff)
            if self.stateController.currentState.key == StateKey.sailingOffExpidition:
                self.stateController.transit(Transitions.selectCombat)
            return Status.normal
        return status
