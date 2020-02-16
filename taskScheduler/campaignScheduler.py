from task.taskKey import TaskKey
from taskScheduler.dailyRoutineScheduler import DailyRoutineScheduler

class CampaignScheduler(DailyRoutineScheduler):
    def __init__(self, taskQueue):
        DailyRoutineScheduler.__init__(self, taskQueue)
        self.refreshTime = [
            time(hour = 0, minute = 5),
        ]
        self.taskKey = (TaskKey.exercise, )
