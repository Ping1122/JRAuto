from task.task import Task
from state.stateKey import StateKey

class Combat(Task):
    def __init__(self):
        self.name = "Combat "
        self.totalBattle = 1
        self.nightBattle = [False, ]
        self.formation = [1, ]
        self.retreatSignal = [None, ]
        self.maxRound = 200
        self.targetState = StateKey.sailingOffCombat
        self.strategy = False
        self.squardon = 0
