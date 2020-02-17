from task.tasks.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class Combat55Boss(Combat):
    def __init__(self):
        super().__init__()
        self.key = TaskKey.combat55Boss
        self.name = "5-5boss submarine"
        self.totalBattle = 3
        self.nightBattle = [False, False, True]
        self.formation = [1, 1, 3]
        self.retreatSignal = [
            (Signals.stage55bossSquardAtA, Signals.stage55bossSquardAtB),
            None,
            None
        ]
        self.maxRound = 10
        self.targetStage = 4
        self.targetMap = 4
        self.squardon = 0
