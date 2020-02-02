from task.combat import Combat

class Combat61a(Combat):
    def __init__(self):
        super().__init__()
        self.name += "6-1a"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [None, ]
