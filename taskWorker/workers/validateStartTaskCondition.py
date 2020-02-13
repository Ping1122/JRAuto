from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.signals import Signals

class ValidateStartTaskCondition(TaskWorker):
    def workDefault(self, status):
        if self.stateController.currentState.key != self.task.targetState:
            return Status.terminate
        return Status.normal

    def workCampaign(self, status):
        if self.stateController.currentState.signal[Signals.noMoreCampaignTrials]:
            return Status.terminate
        return Status.normal

    def workExercise(self, status):
        if self.stateController.currentState.signal[Signals.noMoreExerciseTrials]:
            return Status.terminate
        return Status.normal
