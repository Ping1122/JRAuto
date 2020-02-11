from state.behaviors import Behaviors

class StageSelector:
    def __init__(self):
        pass

    def selectStageAndMap(self, state, targetStage, map):
        return self.selectStage(targetStage) + self.selectMap(map)

    def selectStage(self, state, targetStage):
        procedure = []
        currentStage = state.getStage()
        if currentStage == targetStage:
            if currentStage == 0:
                procedure.append(Behaviors.incrementStage)
                procedure.append(Behaviors.decrementStage)
            else:
                procedure.append(Behaviors.decrementStage)
                procedure.append(Behaviors.incrementStage)
        elif currentStage < targetStage:
            for _ in range(targetStage - currentStage):
                procedure.append(Behaviors.incrementStage)
        else:
            for _ in range(currentStage - targetStage):
                procedure.append(Behaviors.decrementStage)
        return procedure

    def selectMap(self, map):
        procedure = []
        for _ in range(map):
            procedure.append(Behaviors.nextMap)
        return procedure
