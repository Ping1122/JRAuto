from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from state.transitions import Transitions

class StartBattle(TaskWorker):
	def workCombat(self, status):
		if status == Status.normal:
			self.stateController.transit(Transitions.startBattleAtCombatPreparation)
			self.battleIndex = 0
		else:
			self.battleIndex += 1
		return self.battleIndex

	def workCampaign(self, status):
		self.stateController.transit(Transitions.startBattleAtCombatPreparation)
		return status

	def workExercise(self, status):
		self.stateController.transit(Transitions.startBattleAtCombatPreparation)
		return status
