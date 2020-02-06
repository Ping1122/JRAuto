from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from state.stateKey import StateKey
from util.logger import log, Types

class AnalyzeEnemyInfo(TaskWorker):
    def workCombat(self, status):
        if self.stateController.currentState.key != StateKey.enemyInfo:
            return status
        retreatSignal = self.task.retreatSignal[status]
        if retreatSignal and any(self.stateController.currentState.signal[x] for x in retreatSignal):
            message = self.messages.stage74bExistsSubmarineMessage()
            log(message, Types.verbose)
            self.stateController.transit(Transitions.retreatAtEnemyInfo)
            return Status.final
        self.stateController.transit(Transitions.startBattleAtEnemyInfo)
        return status

    def workCampaign(self, status):
        if self.stateController.currentState.key != StateKey.enemyInfo:
            return status
        self.stateController.transit(Transitions.startBattleAtEnemyInfo)
        return status
