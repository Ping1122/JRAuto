from task.tasks.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat74b(Combat):
    def __init__(self):
        super().__init__()
        self.key = TaskKey.combat74b
        self.name += "7-4 B"
        self.nightBattle = [False, ]
        self.formation = [0, ]
        self.maxRound = 50
        self.retreatSignal = [(Signals.stage74bExistsSubmarine, ), ]
        self.targetStage = 6
        self.targetMap = 3
        self.squardon = 2
