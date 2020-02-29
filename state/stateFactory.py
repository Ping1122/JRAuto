from state.stateKey import StateKey
from data.constants import IMG_RESOLUTION
from state.signals import Signals
from state.keyStateMap import keyStateMap
from state.states.unknown import Unknown

class StateFactory:
	def __init__(self):
		pass

	def makeStateByScreenshot(self, screenshot):
		width = screenshot.size[0]
		data = screenshot.getdata()
		stateClass = Unknown
		for state in keyStateMap.values():
			if all(
				self.debug(width, pos, data, color, state)
				for pos, color in state.signature.items()
			):
				stateClass = state
				break
		state = stateClass()
		self.setSignalByScreenshot(state, screenshot)
		return state

	def debug(self, width, pos, data, color, state):
		if state == keyStateMap[StateKey.sailingOffExercise]:
		#if state == Signals.squardon2Selected:
			print(data[pos[1]*width+pos[0]], color)
		print(state,pos[0], pos[1])
		return data[pos[1]*width+pos[0]] in color

	def setSignalByScreenshot(self, state, screenshot):
		width = screenshot.size[0]
		data = screenshot.getdata()
		for key, signature in state.sign.items():
			if all(
				self.debug(width, pos, data, color, key)
				#data[pos[1]*IMG_RESOLUTION[0]+pos[0]] == color
				for pos, color in signature.items()
			):
				state.signal[key] = True
			else:
				state.signal[key] = False
