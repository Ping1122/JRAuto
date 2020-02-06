from task.combat import Combat
from state.signals import Signals

class Combat74b(Combat):
    def __init__(self):
        super().__init__()
        self.name = "7-4b"
        self.nightBattle = [False, ]
        self.formation = [0, ]
        self.maxRound = 50
        self.retreatSignal = [(Signals.stage74bExistsSubmarine, ), ]
