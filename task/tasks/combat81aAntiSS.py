from task.tasks.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat81aAntiSS(Combat):
    def __init__(self):
        super(Combat81aAntiSS, self).__init__()
        self.key = TaskKey.combat81aAntiSS
        self.name += "8-1 A Anti-SS"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage81aExistsCL, Signals.stage81aExistsCA), ]
        self.maxRound = 50
        self.targetStage = 7
        self.targetMap = 0
        self.squardon = 3
