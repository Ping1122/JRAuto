from data.constants import DEFAULT_SCHEDULE_WAIT_TIME
from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey

class DefaultScheduler(Scheduler):
    def __init__(self, taskQueue):
        Scheduler.__init__(self, taskQueue)

    def run(self):
        while self.continue:
            self.taskQueue.emptyEvent.wait()
            if self.taksQueue.nonEmptyEvent.wait(DEFAULT_SCHEDULE_WAIT_TIME):
                continue;
            self.taskQueue.put(Combat81aAntiSubmarine(50), False)
