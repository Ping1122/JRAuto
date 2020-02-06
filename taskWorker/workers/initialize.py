from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.signals import Signals

class Initialize(TaskWorker):
    def workCampaign(self, status):
        if self.stateController.currentState.signal[Signals.noMoreCampaignTrials]:
            return Status.terminate
        return Status.normal
