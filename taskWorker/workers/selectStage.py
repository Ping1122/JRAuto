from random import choice
from taskWorker.taskWorker import TaskWorker
from taskWorker.status import Status
from util.logger import log, Types
from state.transitions import Transitions
from state.behaviors import Behaviors
from state.stateKey import StateKey
from state.signals import Signals

class SelectStage(TaskWorker):
    def workCombat(self, status):
        if self.stateController.currentState.key != StateKey.sailingOffCombat:
            self.stateController.transit(Transitions.selectCombat)
        message = self.messages.startSelectStateMessage(self.task.name, self.stateController.currentState.key)
        log(message, Types.verbose)
        self.stateController.transit(Transitions.selectStage)
        return Status.normal

    def workCampaign(self, status):
        if self.stateController.currentState.key != StateKey.sailingOffCampaign:
            self.stateController.transit(Transitions.selectCampaign)
        message = self.messages.startSelectStateMessage(self.task.name, self.stateController.currentState.key)
        log(message, Types.verbose)
        if self.stateController.currentState.signal[Signals.campaignNormalMode]:
            self.stateController.behave(Behaviors.switchMode)
        if status == Status.normal:
            self.availableCampaign = list(range(5))
        if status == Status.damagedRepeat:
            self.availableCampaign.remove(self.stageIndex)
            log("There was ship damaged selecting from" + str(self.availableCampaign), Types.verbose)
        if self.availableCampaign:
            self.stageIndex = choice(self.availableCampaign)
        else:
            self.stageIndex = choice(list(range(5)))
            self.availableCampaign.append(self.stageIndex)
        self.stateController.transit(Transitions(36+self.stageIndex))
        return self.stageIndex

    def workExercise(self, status):
        stageIndex = -1;
        for i in range(4):
            if self.stateController.currentState.signal[Signals(55+i)]:
                stageIndex = i
                break
        if stageIndex != -1:
            return stageIndex
        self.stateController.behave(Behaviors.scrollUp)
        if self.stageController.currentState.signal[Signals.opponent5Available]:
            return 4
        return Status.terminate
