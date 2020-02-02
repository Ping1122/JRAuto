from task.combat import Combat
from state.signals import Signals

class Combat61a(Combat):
    def __init__(self):
        super().__init__()
        self.name += "6-1a"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage61aExistsCVL, Signals.stage61aExistsCLT), ]
        self.maxRound = 1000
