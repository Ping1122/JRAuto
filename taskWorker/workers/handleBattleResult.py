from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.signals import Signals
from state.transitions import Transitions
from state.stateKey import StateKey

class HandleBattleResult(TaskWorker):
    def workCombat(self, status):
        return self.handleBattleResult(status)

    def workCampaign(self, status):
        if self.stateController.currentState.signal(Signals.noDamagedShip):
            status = Status.normal
        else:
            status = Status.damaged
        self.handleBattleResult(status)
        return status

    def handleBattleResult(self, status):
        self.stateController.transit(Transitions.continue)
        if self.stateController.currentState.key == StateKey.slavagedShip:
            self.stateController.transit(Transitions.continue)
        if self.stateController.currentState.key == StateKey.newShip:
            message = self.messages.lockNewShip()
            log(message, Types.verbose)
            self.stateController.transit(Transitions.confirmAtNewShip)
        if self.stateController.currentState.key == StateKey.sailingOffCombat:
            return Status.normal
        return status
