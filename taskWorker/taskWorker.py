from util.messages import Messages
from status import Status
from task.tasks.combat import Combat
from task.tasks.campaign import Campaign
from task.tasks.exercise import Exercise

class TaskWorker(object):
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
        elif isinstance(self.task, Campaign):
            self.initCampaign()
        elif isinstance(self.task, Exercise):
            self.initExercise()

    def initCombat(self):
        pass

    def initCampaign(self):
        pass

    def initExercise(self):
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
                if status in (Status.terminate, Status.interrupted):
                    return status
            if status not in (Status.repeat, Status.damagedRepeat):
                break
        return status

    def work(self, status):
        resultStatus = self.workDefault(status)
        if resultStatus in (Status.terminate, Status.interrupted):
                    return resultStatus
        if isinstance(self.task, Combat):
            resultStatus = self.workCombat(status)
        elif isinstance(self.task, Campaign):
            resultStatus = self.workCampaign(status)
        elif isinstance (self.task, Exercise):
            resultStatus = self.workExercise(status)
        return resultStatus

    def workDefault(self, status):
        return status

    def workCombat(self, status):
        return status

    def workCampaign(self, status):
        return status

    def workExercise(self, status):
        return status
