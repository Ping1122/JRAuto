from util.messages import Messages
from taskWorker.status import Status
from task.combat import Combat
from task.campaign import Campaign

class TaskWorker:
    def __init__(self, stateController, task):
        self.stateController = stateController
        self.task = task
        self.messages = Messages()
        self.status = Status.normal
        self.workers = []
        self.init()

    def init(self):
        if isinstance(self.task, Combat):
            self.initCombat()
        if isinstance(self.task, Campaign):
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
            if status not in (Status.repeat, Status.damagedRepeat):
                break
        return status

    def work(self, status):
        resultStatus = self.workDefault(status)
        if isinstance(self.task, Combat):
            resultStatus = self.workCombat(status)
        elif isinstance(self.task, Campaign):
            resultStatus = self.workCampaign(status)
        return resultStatus

    def workDefault(self, status):
        return status

    def workCombat(self, status):
        return status

    def workCampaign(self, status):
        return status
