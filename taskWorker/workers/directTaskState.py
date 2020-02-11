from taskWorker.taskWorker import TaskWorker
from pilot.stageSelector import StageSelector
from taskWorker.status import Status

class DirectTaskState(TaskWorker):
    def workDefault(self, status):
        self.stateController.direct(self.task.targetState)
        return Status.normal

    def workCombat(self, status):
        self.stageSelector = StageSelector()
        actions = self.stageSelector.selectStageAndMap(
            self.stateController.currentState,
            self.task.targetStage,
            self.task.targetMap
        )
        self.stateController.performActions(actions)
        return status
