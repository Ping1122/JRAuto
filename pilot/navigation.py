from collections import deque
from state.keyStateMap import keyStateMap

class Navigation:
    def __init__(self):
        pass

    def navigate(self, start, end):
        queue = deque()
        queue.append((start, tuple()))
        visited = {start, }
        while len(queue) != 0:
            stateKey, path = queue.popleft()
            if stateKey == end:
                return path
            transitions = self.getTransitions(stateKey)
            for transition in transitions:
                if transition[1] not in visited:
                    queue.append((transition[1], path+(transition, )))
                    visited.add(transition[1])

    def getTransitions(self, stateKey):
        stateTransitions = keyStateMap[stateKey]().transition
        transitions = []
        for transition, states in stateTransitions.items():
            for state in states[0]:
                transitions.append((transition, state))
        return transitions
