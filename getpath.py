from pilot.navigation import Navigation
from state.stateKey import StateKey

navigator = Navigation()
print(navigator.navigate(StateKey.gameClosed, StateKey.combatPreparationStatistic))
