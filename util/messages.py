from datetime import datetime
from task.keyTaskMap import keyTaskMap

class Messages:
    def __init__(self):
        pass

    def enterStagePrompt(self):
        prompt = ["Enter the stage number you want to level. \n", ]
        prompt.append("Currently support stage are:\n")
        for key in keyTaskMap.keys():
            prompt.append(str(int(key)) + ". " + str(key)[8:] + "\n")
        return "".join(prompt)

    def invalidUserInput(self, taskNum):
        return "The task number:" + str(taskNum) + "is invalid"

    def invalidStageWarning(self, stage):
        return str(stage) + "is not supported, please try again"

    def startLevelStageMessage(self, stage):
        self.time = datetime.now()
        return "Start leveling at" + str(stage)

    def stageCompleteMessage(self, count, stage):
        now = datetime.now()
        timeUsed = (now - self.time).total_seconds()
        return "Completed the" + srt(stage) + " for " + srt(count) + "times. Used " + str(int(timeUsed)) + "seconds"

    def startSelectStateMessage(self, stage, state):
        return "Start selecting" +  str(stage) + ", at screen {str(state)[9:]}"

    def startSupplyMessage(self):
        return "Start to supply ships"

    def existsDamagedShipsWarning(self, damagedShips):
        verb = "is" if len(damagedShips) == 1 else "are"
        return "Ship " + str(list(damagedShips))[1:-1] + str(verb) + " damaged, quick repair it"

    def stage74bExistsSubmarineMessage(self):
        return "There are enemy submarines at 7-4b, retreat"

    def noDamagedShipsMessage(self):
        return "There are no damaged ships, ready to start battle"

    def invalidTransitionOrBehavior(self, type):
        return "Trying to " + str(type) + ", but not in correct screen"

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
        return "Select" + str(formation)[12:] + " formation"
