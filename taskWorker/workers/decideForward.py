from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.signals import Signals
from state.stateKey import StateKey
from state.transitions import Transitions
from util.logger import log, Types

class DecideForward(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.forwardOrRetreat:
            return status
        message = self.messages.decideForward()
        log(message, Types.verbose)
        if self.stateController.currentState.signal[Signals.existsSeriouslyDamagedShip]:
            self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
            return Status.normal
        if (status >= self.task.totalBattle - 1):
            self.stateController.transit(Transitions.retreatAtForwardOrRetreat)
            return Status.normal
        self.stateController.transit(Transitions.forward)
        return Status.repeat
