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
<<<<<<< HEAD
            stageNum = int(input())
            task = self.taskFactory.makeTaskByKey(stageNum)
            if not self.taskQueue.put(task, False):
=======
            try:
                stageNum = int(synchronizedInput(""))
                task = self.taskFactory.makeTaskByKey(stageNum)
            except:
                log("Invalid Input, try again", Types.info)
                continue
            if not self.taskQueue.insert(0, task, False):
>>>>>>> 52af90b1e4b9e13de7fc652d67a17a2e40ffa3fb
                print("taskQueue is full")
