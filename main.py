from controllers.taskController import TaskController
from controllers.schedulerController import SchedulerController
from taskQueue.taskQueue import TaskQueue

def main():
	taskQueue = TaskQueue()
	taskController = TaskController(taskQueue)
	schedulerController = SchedulerController(taskQueue)
	taskController.start()
	schedulerController.startAllSchedulers()

if __name__== "__main__":
	main()
