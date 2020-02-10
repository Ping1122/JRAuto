from datetime import datetime

class Messages:
    def __init__(self):
        pass

    def enterStagePrompt(self):
        prompt = "Enter the stage number you want to level. \n"
        prompt += "Currently support stage are:\n"
        prompt += "1. 5-4 strategy\n"
        prompt += "2. 5-5boss\n"
        prompt += "3. 6-1a submarines\n"
        prompt += "4. 6-1a anti submarines\n"
        prompt += "5. 7-1a\n"
        prompt += "6. 7-4b\n"
        prompt += "7. Campaign"
        return prompt

    def invalidUserInput(self, taskNum):
        return f"The task number: {taskNum} is invalid"

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
        return f"Start selecting {stage}, at screen {str(state)[9:]}"

    def startSupplyMessage(self):
        return "Start to supply ships"

    def existsDamagedShipsWarning(self, damagedShips):
        verb = "is" if len(damagedShips) == 1 else "are"
        return f"Ship {str(list(damagedShips))[1:-1]} {verb} damaged, quick repair it"

    def stage74bExistsSubmarineMessage(self):
        return "There are enemy submarines at 7-4b, retreat"

    def noDamagedShipsMessage(self):
        return "There are no damaged ships, ready to start battle"

    def invalidTransitionOrBehavior(self, type):
        return f"Trying to {str(type)}, but not in correct screen"

    def existsCompletedExpiditionMessage(self):
        return "There exists one or more completed expidition, collecting the resource"

    def analyzeEnemyInfo(self):
        return "Analyzing enemy ships"

    def collectAndRestartExpidition(self):
        return "Collecting then restart the completed Expidition"

    def decideChase(self):
        return "Deciding whether to enter night battle"

    def decideForward(self):
        return "Deciding whether to move to next hold"

    def inspect(self):
        return "Inspecting ships to check demages"

    def lockNewShip(self):
        return "Obtained a new ship. Lock it"

    def retreatFlagShipDamaged(self):
        return "Retreat since the flag ship is seriously damaged"

    def selectFormation(self, formation):
        return f"Select {str(formation)[12:]} formation"
