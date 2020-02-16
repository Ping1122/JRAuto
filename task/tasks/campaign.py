from task.task import Task
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Campaign(Task):
    def __init__(self):
        self.key = TaskKey.campaign
        self.name = "Campaign "
        self.nightBattle = [True, True, True, True, True]
        self.formation = [1, 1, 4, 1, 0]
        self.targetState = StateKey.sailingOffCampaign
