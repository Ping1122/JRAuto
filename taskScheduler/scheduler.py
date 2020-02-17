from threading import Thread
from task.taskFactory import TaskFactory

class Scheduler(Thread):
	def __init__(self, taskQueue):
		Thread.__init__(self)
		self.taskQueue = taskQueue
		self.restart = True
		self.taskFactory = TaskFactory()
