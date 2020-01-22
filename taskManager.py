from gameController import GameController
from logger import log, Types
import message


class TaskManager:
    def __init__():
        this.stages = { "7-1a", "7-4b" }
        this.gameController = GameController()

    def levelStage(stage):
    	if stage not in this.stages:
    		log(message.invaildStage, Types.warning)
    		return
    	count = 0
    	while True:
    		selectStage(stage)
    		inspectRepairReplace()
    		supply()
    		battle(stage)
    		count += 1
    		log("Complete " + stage + " for " + str(count) + " times", Types.info)
