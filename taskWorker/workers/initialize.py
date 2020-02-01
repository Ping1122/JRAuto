from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class Initialize(TaskWorker):
    def work(self, status):
        return Status.normal
