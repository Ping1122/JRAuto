from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.transitToTargetState import TransitToTargetState
from taskWorker.workers.damageControl import DamageControl
from taskWorker.workers.supply import Supply
from taskWorker.workers.battle import Battle
from taskWorker.status import Status

class Execute(TaskWorker):
    def initCombat(self):
        self.addTaskWorkers([
            TransitToTargetState,
            DamageControl,
            Supply,
            Battle,
            CheckExecute,
        ])
