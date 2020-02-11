from state.stateFactory import StateFactory
from state.behaviors import Behaviors
from state.transitions import Transitions
from controllers.mouseController import MouseController
from components.monitor import Monitor
from pilot.navigation import Navigation
from pilot.stateDefaultAction import StateDefaultAction
from util.messages import Messages
from util.logger import log, Types

class StateController:
    def __init__(self):
        self.messages = Messages()
        self.monitor = Monitor()
        self.mouseController = MouseController(self)
        self.stateFactory = StateFactory()
        self.navigation = Navigation()
        self.stateDefaultAction = StateDefaultAction()
        self.currentTask = None
        self.updateState()

    def setCurrentTask(self, task):
        self.currentTask = task

    def updateState(self):
        screenshot = self.monitor.takeScreenshot()
        self.currentState = self.stateFactory.makeStateByScreenshot(screenshot)
        actions = self.stateDefaultAction.getDefaultAction(self.currentState, self.currentTask)
        self.performActions(actions)
        log(str(self.currentState), Types.debug)
        return self.currentState.key

    def transit(self, key):
        if key not in self.currentState.transition:
            message = self.messages.invalidTransitionOrBehavior(key)
            log(message, Types.error)
            exit(1)
        resultStates, clickInfo = self.currentState.transition[key]
        self.mouseController.clickAndWaitUntilStateChange(
            clickInfo,
            self.currentState.key,
            resultStates,
        )

    def behave(self, key):
        if key not in self.currentState.behavior:
            message = self.messages.invalidTransitionOrBehavior(key)
            log(message, Types.error)
            exit(1)
        clickInfo = self.currentState.behavior[key]
        self.mouseController.clickAndNoStageChange(clickInfo)
        self.updateState()

    def performActions(self, keys):
        for key in keys:
            if isinstance(key, Behaviors):
                self.behave(key)
            elif isinstance(key, Transitions):
                self.transit(key)

    def direct(self, targetState):
        if self.currentState.key == targetState:
            return
        path = self.navigation.navigate(self.currentState.key, targetState)
        for transitionKey, nextStateKey in path:
            self.transit(transitionKey)
            if self.currentState.key != nextStateKey:
                self.direct(targetState)
                break
