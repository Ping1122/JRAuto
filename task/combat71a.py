from task.combat import Combat
from state.stateKey import StateKey

class Combat71a(Combat):
    def __init__(self):
        super().__init__()
        self.name = "7-1a"
        self.nightBattle = [True, ]
        self.formation = [4, ]
        self.targetStage = 6
        self.targetMap = 0
        self.squard = 2