from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey

class CheckExecute(TaskWorker):
    def __init__(self, stateController, task):
        super(CheckExecute, self).__init__(stateController, task)
        self.countExecute = 0;

    def work(self, status):
        if self.countExecute > self.task.maxRound:
            return Status.terminate
