from controllers.stateController import StateController

def main():
	stateController = StateController()
	print(stateController.currentState)
	print(stateController.currentState.getDamagedShips())

if __name__== "__main__":
	main()
