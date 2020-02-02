from util.messages import Messages
from taskWorker.status import Status
from task.combat import Combat

class TaskWorker:
    def __init__(self, stateController, task):
        self.stateController = stateController
        self.task = task
        self.messages = Messages()
        self.status = Status.normal
        self.workers = []
        if isinstance(task, Combat):
            self.initCombat()

    def initCombat(self):
        pass

    def addTaskWorkers(self, taskWorkers):
        for taskWorker in taskWorkers:
            self.workers.append(taskWorker(self.stateController, self.task))

    def dispatch(self, status):
        if not self.workers:
            return self.work(status)
        status = Status.initial
        while status != Status.final:
            for worker in self.workers:
                status = worker.dispatch(status)
                if status == Status.final:
                    break
        if status == Status.terminate:
            return status
        return self.status

    def work(self, status):
        pass
