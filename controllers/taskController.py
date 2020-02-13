from task.combatStrategy import CombatStrategy
from task.combat31Ammunition import Combat31Ammunition
from task.combat55boss import Combat55boss
from task.combat61aAntiSubmarine import Combat61aAntiSubmarine
from task.combat61aSubmarine import Combat61aSubmarine
from task.combat71a import Combat71a
from task.combat74b import Combat74b
from task.combat82c import Combat82c
from task.campaign import Campaign
from task.exercise import Exercise
from taskWorker.taskHandler import TaskHandler
from controllers.stateController import StateController
from error.unexpectedGameCloseError import UnexpectedGameCloseError
from util.logger import log, Types

class TaskController:
    def __init__(self):
        self.tasks = [
        	CombatStrategy(),
            Combat31Ammunition(),
        	Combat55boss(),
        	Combat61aSubmarine(),
        	Combat61aAntiSubmarine(),
        	Combat71a(),
        	Combat74b(),
            Combat82c(),
        	Campaign(),
            Exercise(),
        ]
        self.stateController = StateController()

    def startTask(self, taskNum):
        self.currentTask = self.tasks[taskNum-1]
        taskHandler = TaskHandler(self.stateController, self.currentTask)
        self.stateController.setCurrentTask(self.currentTask)
        while True:
	        try:
	            taskHandler.start()
	        except UnexpectedGameCloseError:
	            log("UnexpectedGameCloseError, restart task", Types.error)
	        else:
	        	break
