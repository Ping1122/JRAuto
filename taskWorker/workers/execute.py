from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.selectStage import SelectStage
from taskWorker.workers.selectSquardon import SelectSquardon
from taskWorker.workers.switchStrategy import SwitchStrategy
from taskWorker.workers.damageControl import DamageControl
from taskWorker.workers.supply import Supply
from taskWorker.workers.battle import Battle
from taskWorker.workers.checkExecute import CheckExecute
from taskWorker.workers.handleExpidition import HandleExpidition
from taskWorker.status import Status

class Execute(TaskWorker):
    def initCombat(self):
        self.addTaskWorkers([
            SelectStage,
            SelectSquardon,
            SwitchStrategy,
            DamageControl,
            Supply,
            Battle,
           	HandleExpidition,
            CheckExecute,
        ])

    def initCampaign(self):
    	self.addTaskWorkers([
            SelectStage,
            DamageControl,
            Supply,
            Battle,
            CheckExecute,
        ])

    def initExercise(self):
        self.addTaskWorkers([
            SelectStage,
            SelectSquardon,
            DamageControl,
            Supply,
            Battle,
            CheckExecute,
        ])
