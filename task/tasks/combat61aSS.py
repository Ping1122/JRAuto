from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat61aSS(Combat):
    def __init__(self):
        super().__init__()
        self.key = TaskKey.combat61aSS
        self.name = "6-1a Submarine"
        self.nightBattle = [False, ]
        self.formation = [3, ]
        self.retreatSignal = [None, ]
        self.maxRound = 1000
        self.targetStage = 5
        self.targetMap = 0
        self.squardon = 0
