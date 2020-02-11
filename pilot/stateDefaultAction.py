from state.stateKey import StateKey

class StateDefaultAction:
    def __init__(self):
        self.defaultActionMap = {
        }

    def getDefaultAction(self, state, task):
        if state.key not in self.defaultActionMap:
            return []
        self.state = state
        self.task = task
        return self.defaultActionMap[state.key]()
