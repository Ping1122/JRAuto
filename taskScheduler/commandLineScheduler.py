from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey

class CommandLineScheduler(Scheduler):
    def __init__(self, taskQueue):
        Scheduler.__init__(self, taskQueue)
        self.taskFactory = TaskFactory()

    def run(self):
        while self.continue:
            log(Messages().enterStagePrompt(), Types.info)
			stageNum = int(input())
            task = self.taskFactory.makeTaskByKey(stageNum)
            if not self.taskQueue.put(task, False):
                print("taskQueue is full")
