from task.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat81aAntiSS(Combat):
    def __init__(self, maxRound):
        Combat.__init__(self)
        self.key = TaskKey.combat81aAntiSS
        self.name += "8-1a AntiSubmarine"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage81aExistsCL, Signals.stage81aExistsCA), ]
        self.maxRound = maxRound
        self.targetStage = 7
        self.targetMap = 0
        self.squardon = 3
