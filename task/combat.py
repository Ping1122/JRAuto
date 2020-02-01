from task.task import Task

class Combat(Task):
    def __init__(self):
        self.totalBattle = 1
        self.nightBattle = [False, ]
        self.formation = [1, ]
        self.retreatSignal = [None, ]
        self.maxRound = 200
