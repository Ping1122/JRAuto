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
        if status == Status.normal:
            self.stageIndex = 0
        if status == Status.repeat:
            self.stageIndex += 1
        while self.stageIndex < 4 and not self.stateController.currentState.signal[Signals(55+self.stageIndex)]:
            self.stageIndex += 1
        if self.stageIndex < 4:
            self.stateController.transit(Transitions(45+self.stageIndex))
            self.stateController.transit(Transitions.challenge)
            return self.stageIndex
        if self.stageIndex == 4:
            self.stateController.behave(Behaviors.scrollUp)
            if self.stateController.currentState.signal[Signals.opponent5Available]:
                self.stateController.transit(Transitions(49))
                self.stateController.transit(Transitions.challenge)
                return 4
        return Status.terminate
