from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey

class CheckBattleState(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key == StateKey.sailingOffCombat:
            return Status.final
        return Status.normal
