from state.stateKey import StateKey

class PopStateHandler:
    def __init__(self):
        self.stateActionMap = {
            StateKey.networkDisconnected : self.handleNetworkDisconnected,
            StateKey.newsAndAnnouncement : self.handleNewsAndAnnouncement,
            StateKey.obtainLoginResource : self.handleObtainLoginResource,
            StateKey.attendence : self.handleAttendence,
        }

    def handlePopState(self, state):
        if state.key not in self.stateActionMap:
            return []
        self.state = state
        return self.stateActionsMap[state.key]()
