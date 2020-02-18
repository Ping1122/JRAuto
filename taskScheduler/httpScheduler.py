from server.server import app, init

class HttpScheduler(Scheduler):
    def __init__(self, taskQueue):
        taskQueue.__init__(self, taskQueue)
        self.name = "Http Scheduler"

    def run(self):
        init(self.taskQueue)
        app.run(host = '0.0.0.0', port = 5000)
