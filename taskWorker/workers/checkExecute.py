from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey
from state.signals import Signals

class CheckExecute(TaskWorker):
    def __init__(self, stateController, task):
        super(CheckExecute, self).__init__(stateController, task)
        self.countExecute = 0;

    def workCombat(self, status):
        self.countExecute =+ 1
        if self.countExecute > self.task.maxRound:
            return Status.normal
        return Status.continue

    def workCampaign(self, status):
        if status == Status.damaged:
            return status
        if self.stateController.currentState.signals[Signals.noMoreCampaignTrials]:
            return Status.normal
        return Status.continue
