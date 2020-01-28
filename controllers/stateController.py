from state.stateFactory import StateFactory
from controllers.mouseController import MouseController
from components.monitor import Monitor
from util.messages import Messages
from util.logger import log, Types

class StateController:
    def __init__(self):
        self.messages = Messages()
        self.monitor = Monitor()
        self.mouseController = MouseController(self)
        self.stateFactory = StateFactory()
        self.updateState()

    def updateState(self):
        screenshot = self.monitor.takeScreenshot()
        self.currentState = self.stateFactory.makeStateByScreenshot(screenshot)
        log(str(self.currentState), Types.debug)
        return self.currentState.key

    def transit(self, key):
        if key not in self.currentState.transition:
            message = self.messages.invalidTransitionOrBehavior(key)
            log(message, Types.error)
            exit(1)
        resultStates, clickInfo, clickWhileWaiting = self.currentState.transition[key] 
        self.mouseController.clickAndWaitUntilStateChange(
            clickInfo,
            self.currentState.key,
            resultStates,
            clickWhileWaiting
        )

    def behave(self, key):
        if key not in self.currentState.behavior:
            message = self.messages.invalidTransitionOrBehavior(key)
            log(message, Types.error)
            exit(1)
        clickInfo = self.currentState.behavior[key] 
        self.mouseController.clickAndNoStageChange(clickInfo)
