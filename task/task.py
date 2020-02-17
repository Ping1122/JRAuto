class Task:
    def __init__(self):
        self.name = ""
        self.isHead = False

    def __str__(self):
        head = "Head" if self.isHead else ""
        return f"{head} {self.name}"
