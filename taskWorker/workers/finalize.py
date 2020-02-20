from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status

class Finalize(TaskWorker):
	def work(self, status):
		if status == Status.normal:
			return Status.terminate 
		return status
