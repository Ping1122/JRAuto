from task.tasks.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat81aCVL(Combat):
    def __init__(self):
        super(Combat81aCVL, self).__init__()
        self.key = TaskKey.combat81aCVL
        self.name += "8-1 A CVL"
        self.nightBattle = [False, ]
        self.formation = [4, ]
        self.retreatSignal = [(Signals.stage81aExistsCA, ), ]
        self.maxRound = 50
        self.targetStage = 7
        self.targetMap = 0
        self.squardon = 3
