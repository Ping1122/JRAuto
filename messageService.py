from datetime import datetime

class MessageService:
    def __init__():
        pass

    def enterStagePrompt(stages):
        prompt = ["Enter the stage number you want to level. \nCurrently support stage are:\n"]
        for index, stage in enumerate(stages):
            prompt.append(f"{index+1}. {stage}\n")
        return "".join(prompt)

    def invalidStageWarning(stage):
        return f"{stage} is not supported, please try again"

    def startLevelStageMessage(stage):
        this.time = datatime.now()
        return f"Start leveling at {stage}"

    def stageCompleteMessage(count, stage):
        now = datatime.now()
        timeUsed = (now - this.time).total_seconds()
        this.time = now
        return f"Completed the {stage} for {count} times. Used {timeUsed} seconds"

    def startSelectStateMessage(stage, state):
        return f"Start selecting ${stage}, at screen {str(state[7:])}"

    def inspectRepairReplaceMessage(state):
        return f"Start inspect, repair and replace, at screen {str(state[7:])}"

    def existsDamagedShipsWarning(damagedShips):
        ships = map(damagedShips, lambda x: x+1)
        verb = "is" if len(damagedShips) == 1 else "are"
        return f"Ship {str(ships)[1:-1]} {verb} damaged, leveling stopped"

    def startSupplyMessage(state):
        return f"Start supply ships, at screen {str(state[7:])}"

    def startBattleMessage(stage, state):
        return f"Start battle at ${stage}, at screen {str(state[7:])}"

    def stage74bExistsSubmarineMessage():
        return "There are enemy submarines at 7-4b, retreat"

    def assertStateFailMessage(description):
        return f"Trying to {description} but not in correct screens"
