from task.combat import Combat
from state.signals import Signals

class Combat61aSubmarine(Combat):
    def __init__(self):
        super().__init__()
        self.name += "6-1a Submarine"
        self.nightBattle = [False, ]
        self.formation = [3, ]
        self.retreatSignal = [None, ]
        self.maxRound = 1000
