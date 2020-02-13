from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey

class Combat31Ammunition(Combat):
    def __init__(self):
        super().__init__()
        self.name += "5-4 strategy"
        self.totalBattle = 1
        self.nightBattle = [False, ]
        self.formation = [1, ]
        self.retreatSignal = [None, ]
        self.maxRound = 10
        self.targetStage = 2
        self.targetMap = 0
        self.resource = True
        self.squardon = 2
