from task.combat61aAntiSubmarine import Combat61aAntiSubmarine
from task.combat61aSubmarine import Combat61aSubmarine
from task.combat71a import Combat71a
from task.combat74b import Combat74b
from task.campaign import Campaign
from taskWorker.taskHandler import TaskHandler
from controllers.stateController import StateController

class TaskController:
    def __init__(self):
        self.tasks = [Combat61aSubmarine(), Combat61aAntiSubmarine(), Combat71a(), Combat74b(), Campaign()]
        self.stateController = StateController()

    def startTask(self, taskNum):
        taskHandler = TaskHandler(self.stateController, self.tasks[taskNum-1])
        taskHandler.start()
