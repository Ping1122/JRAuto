from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.inspect import Inspect
from taskWorker.workers.repair import Repair
from taskWorker.workers.replace import Replace
from taskWorker.status import Status

class DamageControl(TaskWorker):
    def __init__(self, stateController, task):
        super(Initializer, self).__init__(stateController, task)

    def initCombat(self):
        self.addTaskWorkers([
            Inspect,
            Repair,
            Replace,
        ])
