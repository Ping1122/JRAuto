from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from util.logger import log, Types

class SelectFormation(TaskWorker):
    def work(self, status):
        index = int(status)-3
        formationIndex = self.task.formation[index]
        message = self.messages.selectFormation(Transitions(formationIndex+15))
        log(message, Types.verbose)
        self.stateController.transit(Transitions(formationIndex+15))
        return status
