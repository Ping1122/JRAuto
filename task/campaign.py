from task.task import Task

class Campaign(Task):
    def __init__(self):
        self.name = "Campaign "
        self.nightBattle = [True, True, True, True, True]
        self.formation = [1, 1, 4, 1, 0]
