from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from state.stateKey import StateKey

class DecideChase(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.chaseOrGiveUp:
            return status
        if not self.task.nightBattle[status]:
            self.stateController.transit(Transitions.giveUp)
        else:
            self.stateController.transit(Transitions.chase)
        return status
