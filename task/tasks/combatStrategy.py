from task.tasks.combat import Combat
from state.signals import Signals
from state.stateKey import StateKey
from task.taskKey import TaskKey

class CombatStrategy(Combat):
    def __init__(self):
        super(CombatStrategy, self).__init__()
        self.key = TaskKey.combatStrategy
        self.name += "6-1 Strategy"
        self.totalBattle = 4
        self.nightBattle = [False, ] * self.totalBattle
        self.formation = [1, ] * self.totalBattle
        self.retreatSignal = [None, ] * self.totalBattle
        self.maxRound = 10
        self.targetStage = 5
        self.targetMap = 0
        self.strategy = True
        self.squardon = 2
