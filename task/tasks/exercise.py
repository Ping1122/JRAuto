from task.task import Task
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Exercise(Task):
	def __init__(self):
		Task.__init__(self)
		self.name = "Exercise "
		self.key = TaskKey.exercise
		self.nightBattle = [True, ] * 5
		self.formation = [0, ] * 5
		self.targetState = StateKey.sailingOffExercise
		self.squardon = 1
