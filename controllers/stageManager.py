from controllers.gameController import GameController
from data.constants import MAX_LEVEL_STAGE_TIMES
from util.logger import log, Types
from util.messages import Messages


class StageManager:
    def __init__(self):
        self.stages = [ "7-1a", "7-4b" ]
        self.gameController = GameController()
        self.messages = Messages()

    def levelStage(self, stageNum):
        if stageNum <= 0 or stageNum > len(self.stages):
            log(self.messages.invalidStageWarning(stage), Types.warning)
            return
        stage = self.stages[stageNum-1]
        log(self.messages.startLevelStageMessage(stage), Types.info)
        for count in range(1, MAX_LEVEL_STAGE_TIMES+1):
            self.gameController.selectStage(stage)
            self.gameController.inspectRepairReplace()
            self.gameController.supply()
            self.gameController.battle(stage)
            log(self.messages.stageCompleteMessage(count, stage), Types.info)
