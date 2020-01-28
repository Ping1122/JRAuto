from datetime import datetime

class Messages:
    def __init__(self):
        pass

    def enterStagePrompt(self, stages):
        prompt = ["Enter the stage number you want to level. \nCurrently support stage are:\n"]
        for index, stage in enumerate(stages):
            prompt.append(f"{index+1}. {stage}\n")
        return "".join(prompt)

    def invalidUserInput(self, stageNum):
        return f"{stageNum} is invalid"

    def invalidStageWarning(self, stage):
        return f"{stage} is not supported, please try again"

    def startLevelStageMessage(self, stage):
        self.time = datetime.now()
        return f"Start leveling at {stage}"

    def stageCompleteMessage(self, count, stage):
        now = datetime.now()
        timeUsed = (now - self.time).total_seconds()
        return f"Completed the {stage} for {count} times. Used {int(timeUsed)} seconds"

    def startSelectStateMessage(self, stage, state):
        return f"Start selecting {stage}, at screen {str(state)[7:]}"

    def inspectRepairReplaceMessage(self, state):
        return f"Start inspect, repair and replace, at screen {str(state)[7:]}"

    def existsDamagedShipsWarning(self, damagedShips):
        ships = map(lambda x: x+1, damagedShips)
        verb = "is" if len(damagedShips) == 1 else "are"
        return f"Ship {str(list(ships))[1:-1]} {verb} damaged, leveling stopped"

    def startSupplyMessage(self, state):
        return f"Start supply ships, at screen {str(state)[7:]}"

    def startBattleMessage(self, stage, state):
        return f"Start battle at {stage}, at screen {str(state)[7:]}"

    def stage74bExistsSubmarineMessage(self):
        return "There are enemy submarines at 7-4b, retreat"

    def noDamagedShipsMessage(self):
        return "There are no damaged ships, ready to start battle"

    def invalidTransitionOrBehavior(self, type):
        return f"Trying to {type}, but not in correct screen"
