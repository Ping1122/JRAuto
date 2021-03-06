from data.constants import DEFAULT_SCHEDULE_WAIT_TIME
from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey

class DefaultScheduler(Scheduler):
    def __init__(self, taskQueue):
        super(DefaultScheduler, self).__init__(taskQueue)
        self.taskFactory = TaskFactory()

    def run(self):
        while self.restart:
            self.taskQueue.emptyEvent.wait()
            if self.taskQueue.nonEmptyEvent.wait(DEFAULT_SCHEDULE_WAIT_TIME):
                continue;
            task = self.taskFactory.makeTaskByKey(TaskKey.combat81aCVL)
            self.taskQueue.put(task, False)
