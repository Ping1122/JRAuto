from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class Replace(TaskWorker):
    def work(self, status):
        return status
