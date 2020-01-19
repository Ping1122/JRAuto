from actions import *

def stage55():
	pass

def stage61():
	pass

def stage71():
	pass

def stage74():
	while True:
		inspectRepairReplace()
		selectStage()
		battle()

def stage81():
	pass

stages = {
		"5-5": stage55,
		"6-1": stage61,
		"7-1": stage71,
		"7-4": stage74,
		"8-1": stage81,
	}