from task.keyTaskMap import keyTaskMap

class TaskFactory():
    def __init__(self):
        pass

    def makeTaskByKey(self, key, args):
        return keyTaskMap[key]()
