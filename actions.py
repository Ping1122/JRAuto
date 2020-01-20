from appscript import *
from config import *
import time
from monitor import *

def inspectRepairReplace():
	pass

def selectStage(stage):
	pass

def battle():
	pass

def openSimulator():
	simulator = app("/Applications/NemuPlayer.app")
	simulator.run()
	isOpen = False;
	while not isOpen:
		time.sleep(START_SIMULATOR_RETRY_TIME)
		
