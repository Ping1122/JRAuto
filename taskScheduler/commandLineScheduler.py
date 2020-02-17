from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey
from util.logger import log, Types
from util.messages import Messages

class CommandLineScheduler(Scheduler):
    def __init__(self, taskQueue):
        Scheduler.__init__(self, taskQueue)
        self.taskFactory = TaskFactory()
        self.name = "CommandLine Scheduler"

    def run(self):
        while self.restart:
            log(Messages().enterStagePrompt(), Types.info)
            stageNum = int(input())
            task = self.taskFactory.makeTaskByKey(stageNum)
            if not self.taskQueue.put(task, False):
                print("taskQueue is full")
