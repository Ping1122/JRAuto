from controllers.stateController import StateController
from state.signals import Signals

def main():
	stateController = StateController()
	print(stateController.currentState)
	for signal in Signals:
		if signal in stateController.currentState.signal:
			print(stateController.currentState.signal[signal])
	

if __name__== "__main__":
	main()
