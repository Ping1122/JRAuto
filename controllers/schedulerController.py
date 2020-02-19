from taskScheduler.defaultScheduler import DefaultScheduler
from taskScheduler.combatStrategyScheduler import CombatStrategyScheduler
from taskScheduler.campaignScheduler import CampaignScheduler
from taskScheduler.exerciseScheduler import ExerciseScheduler
from taskScheduler.commandLineScheduler import CommandLineScheduler
from taskScheduler.httpScheduler import HttpScheduler

class SchedulerController:
    def __init__(self, taskQueue):
        self.taskQueue = taskQueue
        self.schedulers = [
            DefaultScheduler(self.taskQueue),
            CombatStrategyScheduler(self.taskQueue),
            CampaignScheduler(self.taskQueue),
            ExerciseScheduler(self.taskQueue),
            CommandLineScheduler(self.taskQueue),
            HttpScheduler(self.taskQueue),
        ]

    def startAllSchedulers(self):
        for scheduler in self.schedulers:
            scheduler.start()
