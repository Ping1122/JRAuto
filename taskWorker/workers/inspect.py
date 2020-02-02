from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from util.logger import log, Types

class Inspect(TaskWorker):
    def work(self, status):
        message = self.messages.inspect()
        log(message, Types.verbose)
        return self.stateController.currentState.getDamagedShips()
