from gameController import GameController
from logger import log, Types
from messageService import MessageService
from config import MAX_LEVEL_STAGE_TIMES


class StageManager:
    def __init__(self):
        self.stages = { "7-1a", "7-4b" }
        self.gameController = GameController()
        self.messageService = MessageService()

    def levelStage(self, stage):
        log(self.messageService.startLevelStageMessage(stage), Types.info)
        if stage not in self.stages:
            log(self.messageService.invalidStageWarning(stage), Types.warning)
            return
        for count in range(1, MAX_LEVEL_STAGE_TIMES+1):
            self.gameController.selectStage(stage)
            self.gameController.inspectRepairReplace()
            self.gameController.supply()
            self.gameController.battle(stage)
            log(self.messageService.stageCompleteMessage(count, stage), Types.info)
