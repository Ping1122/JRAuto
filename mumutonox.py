from state.stateKey import StateKey
from state.keyStateMap import keyStateMap
from components.monitor import Monitor
from state.signals import Signals
from state.transitions import Transitions
from state.behaviors import Behaviors

def getnoxcolor(pos):
	x = pos[0] + 2
	y = pos[1] - 4
	color = data[y*width + x]
	print(f"({x}, {y}) : ({color},),")

target = StateKey.attendence
state = keyStateMap[target]()
screenshot = Monitor().takeScreenshot()
width = screenshot.size[0]
data = screenshot.getdata()
print("Signature:")
for pos in state.signature.keys():
	getnoxcolor(pos)
for signal in state.signal.keys():
	print(Signals(singal))
	for pos in signal:
		getnoxcolor(pos)
for transition, info in state.transition.items():
	print(Transitions(transition))
	pos = info[1]
	print(f"({pos[0]+2}, {pos[1]-4}, {pos[2]})")
for behavior, info in state.behavior.items():
	print(Behaviors(behavior))
	pos = info
	print(f"({pos[0]+2}, {pos[1]-4}, {pos[2]})")


