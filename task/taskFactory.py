from keyTaskMap import keyTaskMap
from error.invalidTaskKeyError import InvalidTaskKeyError

class TaskFactory():
    def __init__(self):
        pass

    def makeTaskByKey(self, key):
    	if key not in keyTaskMap:
    		raise InvalidTaskKeyError
        return keyTaskMap[key]()
