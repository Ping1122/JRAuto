from data.constants import DEFAULT_SCHEDULE_WAIT_TIME
from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey

class DefaultScheduler(Scheduler):
    def __init__(self, taskQueue):
        Scheduler.__init__(self, taskQueue)
        self.taskFactory = TaskFactory()
        self.taskKeys = (TaskKey.combat81aCVL, )
        self.name = "Default Scheduler"

    def run(self):
        while self.restart:
            self.taskQueue.emptyEvent.wait()
            if self.taskQueue.nonEmptyEvent.wait(DEFAULT_SCHEDULE_WAIT_TIME):
                continue;
            for taskKey in self.taskKeys:
            	task = self.taskFactory.makeTaskByKey(taskKey)
            	self.taskQueue.put(task, False)
