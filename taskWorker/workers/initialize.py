from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.directTaskState import DirectTaskState
from taskWorker.workers.validateStartTaskCondition import ValidateStartTaskCondition

class Initialize(TaskWorker):
    def init(self):
        self.addTaskWorkers([
            DirectTaskState,
            ValidateStartTaskCondition,
        ])
