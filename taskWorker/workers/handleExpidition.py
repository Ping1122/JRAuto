from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.collectAndRestartExpidition import CollectAndRestartExpidition
from taskWorker.workers.selectExpidition import SelectExpidition
from taskWorker.workers.selectCombat import SelectCombat
from taskWorker.status import Status

class HandleExpidition(TaskWorker):
    def initCombat(self):
        self.addTaskWorkers([
            SelectExpidition,
            CollectAndRestartExpidition,
            SelectCombat,
        ])
        self.status = Status.normal
