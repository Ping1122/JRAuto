from task.keyTaskMap import keyTaskMap

class TaskFactory():
    def __init__(self):
        pass

    def makeTaskByKey(self, key):
        return keyTaskMap[key]()
