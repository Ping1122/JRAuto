from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class Initialize(TaskWorker):
    def workCampaign(self, status):
        if self.stateController.currentState.signals[Signals.noMoreCampaignTrials]:
            return Status.terminate
        return Status.normal
