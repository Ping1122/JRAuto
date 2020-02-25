from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey
from util.logger import log, Types
from util.messages import Messages
from util.functions import synchronizedInput

class CommandLineScheduler(Scheduler):
    def __init__(self, taskQueue):
        super(CommandLineScheduler, self).__init__(taskQueue)
        self.taskFactory = TaskFactory()
        self.name = "CommandLine Scheduler"

    def run(self):
        while self.restart:
            log(Messages().enterStagePrompt(), Types.info)
            try:
                stageNum = int(synchronizedInput(""))
                task = self.taskFactory.makeTaskByKey(stageNum)
            except:
                log("Invalid Input, try again", Types.info)
                continue
            if not self.taskQueue.insert(0, task, False):
                print("taskQueue is full")
