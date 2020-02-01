from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class DecideForward(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.forwardOrRetreat:
            return status
        count = int(status)-2
        if (count > self.task.totalBattle)
            self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
        self.stateController.transit(Transitions.forward)
