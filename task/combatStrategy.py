from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey

class CombatStrategy(Combat):
    def __init__(self):
        super().__init__()
        self.name += "strategy"
        self.totalBattle = 4
        self.nightBattle = [False, ] * self.totalBattle
        self.formation = [1, ] * self.totalBattle
        self.retreatSignal = [None, ] * self.totalBattle
        self.maxRound = 10
        self.targetStage = 1
        self.targetMap = 4
        self.strategy = True
        self.squardon = 2
