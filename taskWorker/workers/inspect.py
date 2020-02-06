from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from util.logger import log, Types

class Inspect(TaskWorker):
    def workCombat(self, status):
        message = self.messages.inspect()
        log(message, Types.verbose)
        return self.stateController.currentState.getDamagedShips()

    def workCampaign(self, status):
        message = self.messages.inspect()
        log(message, Types.verbose)
        damagedShips = self.stateController.currentState.getDamagedShips()
        return (damagedShips, status)
