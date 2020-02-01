class TaskController:
    def __init__(self):
        self.tasks = [Combat71a(), Combat74b()]

    def startTask(self, taskNum):
        taskHandler = TaskHandler(task)
        taskHandler.start(self.tasks[taskNum+1])
