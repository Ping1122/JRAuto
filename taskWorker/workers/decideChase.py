from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions

class DecideChase(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.chaseOrGiveUp:
            return status
        index = int(status)-3
        if not self.task.nightBattle(index):
            self.stateController.transit(Transitions.giveUp)
        else:
            self.stateController.transit(Transitions.chase)
        return status
