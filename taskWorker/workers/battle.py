from taskWorker.taskWorker import TaskWorker
from taskWorker.workers.startBattle import StartBattle
from taskWorker.workers.analyzeEnemyInfo import AnalyzeEnemyInfo
from taskWorker.workers.selectFormation import SelectFormation
from taskWorker.workers.decideChase import DecideChase
from taskWorker.workers.handleBattleResult import HandleBattleResult
from taskWorker.workers.retreatFlagShipDamaged import RetreatFlagShipDamaged
from taskWorker.workers.decideForward import DecideForward
from taskWorker.status import Status

class Battle(TaskWorker):
    def init(self):
        self.addTaskWorkers([
            StartBattle,
            AnalyzeEnemyInfo,
            SelectFormation,
            DecideChase,
            HandleBattleResult,
            RetreatFlagShipDamaged,
            DecideForward,
        ])
