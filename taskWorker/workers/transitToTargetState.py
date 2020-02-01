from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class TransitToTargetState(TaskWorker):
    def work(self, status):
        message = self.messages.startSelectStateMessage(stage, self.stateController.currentState.key)
        log(message, Types.verbose)
        self.stateController.transit(Transitions.selectStage)
        return Status.normal
