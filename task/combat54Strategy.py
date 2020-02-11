from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey

class Combat54Strategy(Combat):
    def __init__(self):
        super().__init__()
        self.name += "5-4 strategy"
        self.totalBattle = 3
        self.nightBattle = [False, False, False]
        self.formation = [1, 1, 1]
        self.retreatSignal = [None, None, None]
        self.maxRound = 10
        self.targetStage = 4
        self.targetMap = 3
