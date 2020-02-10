from state.behaviors import behaviors

class StateSelector:
    def __init__(self):
        pass

    def selectStageAndMap(self, state, targetStage, map):
        return self.selectStage(targetState) + self.selectMap(map)

    def selectStage(self, state, targetState):
        procedure = []
        currentState = state.getState()
        if currentState == targetState:
            if currentState == 0:
                procedure.append(Behaviors.incrementStage)
                procedure.append(Behaviors.decrementStage)
            else:
                procedure.append(Behaviors.decrementStage)
                procedure.append(Behaviors.incrementStage)
        elif currentState < targetState:
            for _ in range(targetState - currentState):
                procedure.append(Behaviors.incrementStage)
        else:
            for _ in range(currentState - targetState):
                procedure.append(Behaviors.decrementStage)
        return procedure

    def selectMap(self, map):
        procedure = []
        for _ in range(map):
            procedure.append(Behaviors.nextMap)
        return procedure
