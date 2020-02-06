from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey
from state.transitions import Transitions
from state.signals import Signals

class CollectAndRestartExpidition(TaskWorker):
	def work(self, status):
		if status == Status.normal:
			return status
		for i in range(4):
			if self.stateController.currentState.signal[Signals(i+8)]:
				self.stateController.transit(Transitions(i+29))
				self.stateController.transit(Transitions.nextState)
				self.stateController.transit(Transitions.confirmAtContinueExpidition)
		return Status.repeat
