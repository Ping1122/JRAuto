from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.stateKey import StateKey
from state.transitions import Transitions
from state.signals import Signals
from util.logger import log, Types

class SelectExpidition(TaskWorker):
	def work(self, status):
		if self.stateController.currentState.signal[Signals.existsCompletedExpidition]:
			message = self.messages.existsCompletedExpiditionMessage()
			log(message, Types.verbose)
			if self.stateController.currentState.key != StateKey.sailingOffExpidition:
				self.stateController.transit(Transitions.selectExpidition)
			return Status.normal
		return Status.final
