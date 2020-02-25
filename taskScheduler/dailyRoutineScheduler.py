from datetime import datetime, date, time, timedelta
from time import sleep
from taskScheduler.scheduler import Scheduler
from task.taskFactory import TaskFactory
from task.taskKey import TaskKey
from util.functions import linearSearch

class DailyRoutineScheduler(Scheduler):
    def __init__(self, taskQueue):
        super(DailyRoutineScheduler, self).__init__(taskQueue)
        self.refreshTime = [
            time(hour = 0, minute = 5),
        ]
        self.initial = True

    def run(self):
        while self.restart:
            if self.initial:
                self.initial = False
            else:
                if len(self.taskKeys) == 1:
                    task = self.taskFactory.makeTaskByKey(self.taskKeys[0])
                    self.taskQueue.insert(0, task)
                else:
                    for taskKey in self.taskKeys:
                        task = self.taskFactory.makeTaskByKey(taskKey)
                        self.taskQueue.put(task, True)
            currentTime = (datetime.utcnow() + timedelta(hours = 8)).time()
            currentIndex = linearSearch(self.refreshTime, currentTime)
            if currentIndex != len(self.refreshTime):
                endTime = datetime.combine(date.min, self.refreshTime[currentIndex])
                beginTime = datetime.combine(date.min, currentTime)
                sleepTime = (endTime - beginTime).seconds
            else:
                endTime = datetime.combine(date.min, time.max)
                beginTime = datetime.combine(date.min, currentTime)
                sleepTime = (endTime - beginTime).seconds
                endTime = datetime.combine(date.min, self.refreshTime[0])
                beginTime = datetime.combine(date.min, time.min)
                sleepTime += (endTime - beginTime).seconds
            print(self.name + ": will wake up after " + str(sleepTime))
            sleep(sleepTime)
