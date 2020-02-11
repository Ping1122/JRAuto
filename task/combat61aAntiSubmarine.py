from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey

class Combat61aAntiSubmarine(Combat):
    def __init__(self):
        super().__init__()
        self.name += "6-1a Anti Submarine"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage61aExistsCVL, Signals.stage61aExistsCLT), ]
        self.maxRound = 1000
        self.targetStage = 5
        self.targetMap = 0
