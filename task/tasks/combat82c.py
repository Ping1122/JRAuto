from task.tasks.combat import Combat
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat82c(Combat):
    def __init__(self):
        super(Combat82c, self).__init__()
        self.key = TaskKey.combat82c
        self.name += "8-2 C"
        self.nightBattle = [False, ]
        self.formation = [0, ]
        self.maxRound = 100
        self.targetStage = 7
        self.targetMap = 1
        self.squardon = 0
