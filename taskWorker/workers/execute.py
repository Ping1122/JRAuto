from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.selectStage import SelectStage
from taskWorker.workers.damageControl import DamageControl
from taskWorker.workers.supply import Supply
from taskWorker.workers.battle import Battle
from taskWorker.workers.checkExecute import CheckExecute
from taskWorker.workers.handleExpidition import HandleExpidition
from taskWorker.status import Status

class Execute(TaskWorker):
    def init(self):
        self.addTaskWorkers([
        	HandleExpidition,
            SelectStage,
            DamageControl,
            Supply,
            Battle,
            CheckExecute,
        ])
