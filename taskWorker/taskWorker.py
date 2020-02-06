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
        self.init(self)

    def init(self):
        if isinstance(task, Combat):
            self.initCombat()
        if isinstance(task, Campaign):
            self.initCampaign()

    def initCombat(self):
        pass

    def initCampaign(self):
        pass

    def addTaskWorkers(self, taskWorkers):
        for taskWorker in taskWorkers:
            self.workers.append(taskWorker(self.stateController, self.task))

    def dispatch(self, status):
        if not self.workers:
            return self.work(status)
        while True:
            for worker in self.workers:
                status = worker.dispatch(status)
                if status == Status.terminate:
                    return status
            if status not in (Status.continue, Status.damaged):
                break
        return status

    def work(self, status):
        if isinstance(task, Combat):
            return self.workCombat(status)
        if isinstance(task, Campaign):
            return self.workCampaign(status)

    def workCombat(self, status):
        return status

    def workCampaign(self, status):
        return status
