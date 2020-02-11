from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.signals import Signals
from state.behaviors import Behaviors
from state.transitions import Transitions

class SwitchStrategy(TaskWorker):
    def workCombat(self, status):
        if not self.task.strategy:
        	if self.stateController.currentState.signal[Signals.strategyEnabled]:
        		self.stateController.performActions([
	        		Transitions.selectStrategy,
	        		Behaviors.switchStrategy,
	        		Transitions.backToCombatPreparation,
	        	])
        	return status
        if self.stateController.currentState.signal[Signals.strategyExhausted]:
        	return Status.terminate
        if self.stateController.currentState.signal[Signals.strategyDisabled]:
        	self.stateController.performActions([
        		Transitions.selectStrategy,
        		Behaviors.switchStrategy,
        		Transitions.backToCombatPreparation,
        	])
        return status
