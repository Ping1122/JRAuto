from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from state.stateKey import StateKey
from util.logger import log, Types

class SelectFormation(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key != StateKey.selectFormation:
            return status
        formationIndex = self.task.formation[status]
        message = self.messages.selectFormation(Transitions(formationIndex+15))
        log(message, Types.verbose)
        self.stateController.transit(Transitions(formationIndex+15))
        return status
