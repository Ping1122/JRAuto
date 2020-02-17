from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class Finalize(TaskWorker):
    def work(self, status):
        return status
