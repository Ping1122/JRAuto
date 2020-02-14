from state.stateKey import StateKey
from state.behaviors import Behaviors
from state.transitions import Transitions

class PopStateHandler:
    def __init__(self):
        self.stateActionMap = {
            StateKey.networkDisconnected : self.handleNetworkDisconnected,
            StateKey.newsAndAnnouncement : self.handleNewsAndAnnouncement,
            StateKey.obtainLoginResource : self.handleObtainLoginResource,
            StateKey.attendence : self.handleAttendence,
            StateKey.obtainCombatResource : self.handleObtainCombatResource,
        }

    def handlePopState(self, state):
        if state.key not in self.stateActionMap:
            return []
        self.state = state
        return self.stateActionMap[state.key]()

    def handleNetworkDisconnected(self):
        return [Transitions.confirm, ]

    def handleNewsAndAnnouncement(self):
        return [Behaviors.checkNoNewsToday, Transitions.close]

    def handleObtainLoginResource(self):
        return [Transitions.obtainResource, ]

    def handleAttendence(self):
        return [Transitions.confirm, ]

    def handleObtainCombatResource(self):
        return [Transitions.confirm, ]
