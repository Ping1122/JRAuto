class Task(object):
    def __init__(self):
        self.name = ""
        self.isHead = False
        self.id = 0

    def __str__(self):
        head = "Head" if self.isHead else ""
        return head + str(self.name)
