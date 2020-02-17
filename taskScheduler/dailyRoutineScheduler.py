from datetime import datetime, time
from time import sleep
from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey
from util.functions import linearSearch

class DailyRoutineScheduler(Scheduler):
    def __init__(self, taskQueue):
        Scheduler.__init__(self, taskQueue)
        self.refreshTime = [
            time(hour = 0, minute = 5),
        ]
        self.initial = False

    def run(self):
        while self.continue:
            if self.initial:
                self.initial = False
            else:
                if len(self.taskKeys) == 0:
                    task = self.taskFactory.makeTaskByKey(self.taskKeys[0])
                    self.taskQueue.insert(0, task)
                else:
                    for taskKey in self.taskKeys:
                        task = self.taskFactory.makeTaskByKey(taskKey)
                        self.taskQueue.put(task, True)
            currentTime = (datetime.utcnow() + timedelta(hours = 8)).time()
            currentIndex = linearSearch(self.refreshTime, currentTime)
            if currentIndex != len(self.refreshTime):
                sleepTime = (self.refreshTime[currentIndex] - currentTime).seconds
            else:
                sleepTime = (time.max - currentTime).seconds
                sleepTime += self.refreshTime[0] - time.min
            sleep(sleepTime)
