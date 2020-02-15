from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey

class Combat81aAntiSubmarine(Combat):
    def __init__(self):
        super().__init__()
        self.name += "8-1a AntiSubmarine"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage81aExistsCL, Signals.stage81aExistsCA), ]
        self.maxRound = 1000
        self.targetStage = 7
        self.targetMap = 0
        self.squardon = 3
