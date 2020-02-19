from server.server import app, init
from taskScheduler.scheduler import Scheduler

class HttpScheduler(Scheduler):
    def __init__(self, taskQueue):
        Scheduler.__init__(self, taskQueue)
        self.name = "Http Scheduler"

    def run(self):
        init(self.taskQueue)
        app.run( port = 5000)
