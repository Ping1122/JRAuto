from gameController import GameController
from logger import log, Types
import message


class TaskManager:
    def __init__(self):
        self.stages = { "7-1a", "7-4b" }
        self.gameController = GameController()

    def levelStage(self, stage):
    	if stage not in self.stages:
    		log(message.invalidStage, Types.warning)
    		return
    	count = 0
    	while True:
    		self.gameController.selectStage(stage)
    		self.gameController.inspectRepairReplace()
    		self.gameController.supply()
    		self.gameController.battle(stage)
    		count += 1
    		log("Complete " + stage + " for " + str(count) + " times", Types.info)
