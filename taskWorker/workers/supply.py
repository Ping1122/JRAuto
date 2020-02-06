from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from util.logger import log, Types
from state.stateKey import StateKey
from state.transitions import Transitions
from state.behaviors import Behaviors

class Supply(TaskWorker):
    def work(self, status):
        message = self.messages.startSupplyMessage()
        log(message, Types.verbose)
        if self.stateController.currentState.existsShipNeedSupply():
	        if self.stateController.currentState.key !=  StateKey.combatPreparationQuickSupply:
	            self.stateController.transit(Transitions.selectQuickSupply)
	        self.stateController.behave(Behaviors.supplyAllShips)
        return status
