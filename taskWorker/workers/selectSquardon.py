from taskWorker.taskWorker import TaskWorker
from state.signals import Signals
from state.behaviors import Behaviors

class SelectSquardon(TaskWorker):
    def workCombat(self, status):
        if not self.stateController.currentState.signal[Signals(self.task.squardon+47)]:
        	self.stateController.behave(Behaviors(self.task.squardon+2))
        return status
