from task.tasks.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat61aAntiSS(Combat):
    def __init__(self):
        super().__init__()
        self.key = TaskKey.combat61aAntiSS
        self.name += "6-1 A Anti-SS"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage61aExistsCVL, Signals.stage61aExistsCLT), ]
        self.maxRound = 1000
        self.targetStage = 5
        self.targetMap = 0
        self.targetPoint = "A"
        self.squardon = 3
