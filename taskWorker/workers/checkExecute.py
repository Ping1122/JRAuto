from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey
from state.signals import Signals

class CheckExecute(TaskWorker):
    def __init__(self, stateController, task):
        super(CheckExecute, self).__init__(stateController, task)
        self.countExecute = 0;

    def workDefault(self, status):
        if not self.task.isHead:
            return Status.interrupted
        return status

    def workCombat(self, status):
        self.countExecute += 1
        print(self.countExecute)
        if self.countExecute >= self.task.maxRound:
            return Status.normal
        return Status.repeat

    def workCampaign(self, status):
        if status == Status.damaged:
            return status.damagedRepeat
        if self.stateController.currentState.signal[Signals.noMoreCampaignTrials]:
            return Status.normal
        return Status.repeat

    def workExercise(self, status):
        if status == 4:
            return Status.normal
        return Status.repeat
