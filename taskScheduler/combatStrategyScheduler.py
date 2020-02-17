from task.taskKey import TaskKey
from taskScheduler.dailyRoutineScheduler import DailyRoutineScheduler
from datetime import time

class CombatStrategyScheduler(DailyRoutineScheduler):
    def __init__(self, taskQueue):
        DailyRoutineScheduler.__init__(self, taskQueue)
        self.refreshTime = [
            time(hour = 0, minute = 5),
        ]
        self.taskKeys = (TaskKey.combatStrategy, )
        self.name = "Combat Strategy Handler"
