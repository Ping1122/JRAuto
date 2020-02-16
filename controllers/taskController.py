from task.tasks.combatStrategy import CombatStrategy
from task.tasks.combat31Ammunition import Combat31Ammunition
from task.tasks.combat55boss import Combat55boss
from task.tasks.combat61aAntiSubmarine import Combat61aAntiSubmarine
from task.tasks.combat61aSubmarine import Combat61aSubmarine
from task.tasks.combat71a import Combat71a
from task.tasks.combat74b import Combat74b
from task.tasks.combat81aAntiSubmarine import Combat81aAntiSubmarine
from task.tasks.combat82c import Combat82c
from task.tasks.campaign import Campaign
from task.tasks.exercise import Exercise
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
            Combat81aAntiSubmarine(1000),
            Combat82c(),
        	Campaign(),
            Exercise(),
        ]

    def startTask(self, taskNum):
        self.stateController = StateController()
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
