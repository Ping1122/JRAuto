from taskWorker.status import Status
from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.initialize import Initialize
from taskWorker.workers.execute import Execute
from taskWorker.workers.finalize import Finalize

class TaskHandler(TaskWorker):
    def initCombat(self):
        self.addTaskWorkers([
            Initialize,
            Execute,
            Finalize,
        ])

    def start(self):
        self.dispatch(Status.normal)
