from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions
from state.stateKey import StateKey

class LockNewShip(TaskWorker):
    def work(self, status):
        if self.stateController.currentState.key == StateKey.newShip:
            self.stateController.transit(Transitions.confirmAtNewShip)
        return status
