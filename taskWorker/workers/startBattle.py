from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class StartBattle(TaskWorker):
    def work(self, status):
        if status == Status.initial
            self.stateController.transit(Transitions.startBattleAtEnemyInfo)
            return Status.firstBattle
        return Status(int(status)+1)
