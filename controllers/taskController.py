from task.combat71a import Combat71a
from task.combat74b import Combat74b
from taskWorker.taskHandler import TaskHandler
from controllers.stateController import StateController

class TaskController:
    def __init__(self):
        self.tasks = [Combat71a(), Combat74b()]
        self.stateController = StateController()

    def startTask(self, taskNum):
        taskHandler = TaskHandler(self.stateController, self.tasks[taskNum-1])
        taskHandler.start()
