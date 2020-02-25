from task.tasks.combat import Combat
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat71a(Combat):
	def __init__(self):
		super(Combat71a, self).__init__()
		self.key = TaskKey.combat71a
		self.name += "7-1 A"
		self.nightBattle = [True, ]
		self.formation = [4, ]
		self.targetStage = 6
		self.targetMap = 0
		self.squard = 2
