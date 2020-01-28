from controllers.activityController import ActivityController
from data.constants import MAX_LEVEL_STAGE_TIMES
from util.logger import log, Types
from util.messages import Messages


class GameController:
    def __init__(self):
        self.stages = [ "7-1a", "7-4b" ]
        self.activityController = ActivityController()
        self.messages = Messages()

    def levelStage(self, stageNum):
        if stageNum <= 0 or stageNum > len(self.stages):
            log(self.messages.invalidStageWarning(stage), Types.warning)
            return
        stage = self.stages[stageNum-1]
        log(self.messages.startLevelStageMessage(stage), Types.info)
        for count in range(1, MAX_LEVEL_STAGE_TIMES+1):
            self.activityController.selectStage(stage)
            self.activityController.inspectRepairReplace()
            self.activityController.supply()
            self.activityController.battle(stage)
            log(self.messages.stageCompleteMessage(count, stage), Types.info)
