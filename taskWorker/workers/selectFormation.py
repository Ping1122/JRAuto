from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class selectFormation(TaskWorker):
    def work(self, status):
        index = int(status)-3
        formationIndex = task.formation[index]
        self.stateController.transit(Transitions(formationIndex+15))
        return status
