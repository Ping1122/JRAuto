from threading import Thread
from task.taskFactory import TaskFactory

class Scheduler(Thread):
    def __init__(self, taskQueue):
        self.taskQueue = taskQueue
        self.continue = True
        self.taskFactory = TaskFactory()
