from taskScheduler.defaultScheduler import DefaultScheduler
from taskScheduler.combatStrategyScheduler import CombatStrategyScheduler
from taskScheduler.campaignScheduler import CampaignScheduler
from taskScheduler.exerciseScheduler import ExerciseScheduler

class SchedulerController:
    def __init__(self, taskQueue):
        this.taskQueue = taskQueue
        this.schedulers = [
            DefaultScheduler(self.taskQueue),
            CombatStrategyScheduler(self.taskQueue),
            CampaignScheduler(self.taskQueue),
            ExerciseScheduler(self.taskQueue),
        ]

    def startAllSchedulers(self):
        for scheduler in self.schedulers:
            scheduler.start()
