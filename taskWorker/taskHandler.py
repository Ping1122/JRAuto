from status import Status
from taskWorker import TaskWorker
from workers.initialize import Initialize
from workers.execute import Execute
from workers.finalize import Finalize

class TaskHandler(TaskWorker):
    def init(self):
        self.addTaskWorkers([
            Initialize,
            Execute,
            Finalize,
        ])

    def start(self):
        return self.dispatch(Status.normal)
