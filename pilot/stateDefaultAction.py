from state.stateKey import StateKey

class StateDefaultAction:
    def __init__(self):
        self.defaultActionMap = {
        }

    def getDefaultAction(self, state):
        if state.key not in self.defaultActionMap:
            return []
        self.state = state
        return self.defaultActionMap[state.key]()
