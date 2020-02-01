from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from util.logger import log, Types

class AnalyzeEnemyInfo(TaskWorker):
    def work(self, status):
        index = int(status)-3
        retreatSignal = self.task.retreatSignal[index]
        if retreatSignal and self.stateController.currentState.signal[retreatSignal]:
            message = self.messages.stage74bExistsSubmarineMessage()
            log(message, Types.verbose)
            self.stateController.transit(Transitions.retreatAtEnemyInfo)
            return Status.final
        self.stateController.transit(Transitions.startBattleAtEnemyInfo)
        return status
