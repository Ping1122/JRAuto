from task.task import Task
from state.stateKey import StateKey

class Exercise(Task):
    def __init__(self):
        self.name = "Exercise "
        self.nightBattle = True
        self.formation = 0
        self.targetState = StateKey.sailingOffExercise
