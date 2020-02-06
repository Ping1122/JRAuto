from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions

class SelectCombat(TaskWorker):
    def work(self, status):
    	if status == Status.normal:
    		return status
    	self.stateController.transit(Transitions.selectCombat)
    	return status
