from state.stateFactory import StateFactory
from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions
from controllers.mouseController import MouseController
from components.monitor import Monitor
from pilot.navigation import Navigation
from pilot.popStateHandler import PopStateHandler
from util.messages import Messages
from util.logger import log, Types
from error.unexpectedGameCloseError import UnexpectedGameCloseError
from error.directFromUnknownStateError import DirectFromUnknownStateError

class StateController:
    def __init__(self):
        self.messages = Messages()
        self.monitor = Monitor()
        self.mouseController = MouseController(self)
        self.stateFactory = StateFactory()
        self.navigation = Navigation()
        self.popStateHandler = PopStateHandler()
        self.currentTask = None
        self.currentState = None
        self.handleStateChange()

    def setCurrentTask(self, task):
        self.currentTask = task

    def handleStateChange(self):
        self.updateState()
        self.checkState()
        self.handlePopState()
        return self.currentState.key

    def updateState(self):
        screenshot = self.monitor.takeScreenshot()
        self.previousState = self.currentState
        self.currentState = self.stateFactory.makeStateByScreenshot(screenshot)
        log(str(self.currentState), Types.debug)

    def checkState(self):
        if (
            self.currentState.key == StateKey.gameClosed and
            self.previousState and
            self.previousState.key != StateKey.quitGame and
            self.previousState.key != StateKey.gameClosed
        ):
            raise UnexpectedGameCloseError

    def handlePopState(self):
        if self.previousState and self.previousState.key != self.currentState.key:
            actions = self.popStateHandler.handlePopState(self.currentState)
            self.performActions(actions)

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
        mouseInfo = self.currentState.behavior[key]
        if len(mouseInfo) == 3:
            self.mouseController.clickAndNoStageChange(mouseInfo)
        elif len(mouseInfo) == 2:
            self.mouseController.scrollAndNoStageChange(mouseInfo)
        self.handleStateChange()

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
        if not path:
            raise DirectFromUnknownStateError
        for transitionKey, nextStateKey in path:
            self.transit(transitionKey)
            if self.currentState.key != nextStateKey:
                self.direct(targetState)
                break
