from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey
from state.transitions import Transitions
from util.logger import log, Types

class DecideForward(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.forwardOrRetreat:
            return status
        count = int(status)-2
        message = self.messages.decideForward()
        log(message, Types.verbose)
        if (count >= self.task.totalBattle):
            self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
            return Status.final
        self.stateController.transit(Transitions.forward)
