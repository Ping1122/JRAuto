from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions

class StartBattle(TaskWorker):
	def work(self, status):
		if status == Status.initial:
			self.stateController.transit(Transitions.startBattleAtCombatPreparation)
			return Status.firstBattle
		return Status(int(status)+1)
