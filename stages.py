from actions import *
from logger import *

def startStage74():
	while True:
		selectStage("7-4")
		inspectRepairReplace()	
		supply()
		battle()

stages = {
	"7-4": startStage74,
}