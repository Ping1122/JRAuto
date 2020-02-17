from threading import Thread
from controllers.stateController import StateController
from error.unexpectedGameCloseError import UnexpectedGameCloseError
from taskWorker.status import Status
from taskWorker.taskHandler import TaskHandler
from util.logger import log, Types

class TaskController(Thread):
	def __init__(self, taskQueue):
		Thread.__init__(self)
		self.taskQueue = taskQueue
		self.restart = True

	def run(self):
		while self.restart:
			self.taskQueue.nonEmptyEvent.wait()
			self.currentTask = self.taskQueue.getHead()
			if not self.currentTask:
				continue
			status = self.startTask()
			if status == Status.terminate:
				self.taskQueue.removeByReference(self.currentTask)
			if status == Status.interrupted:
				print("task is interrupted, start another task")

	def startTask(self):
		self.stateController = StateController()
		taskHandler = TaskHandler(self.stateController, self.currentTask)
		self.stateController.setCurrentTask(self.currentTask)
		while True:
			try:
				result = taskHandler.start()
			except UnexpectedGameCloseError:
				log("UnexpectedGameCloseError, restart task", Types.error)
			else:
				break
		return result
