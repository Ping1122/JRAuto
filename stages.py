from actions import *
from logger import *

def startStage(stage):
	if stage not in stages:
		log(message.invaildStage, Types.warning)
		return
	updateScreenshotAndState()
	while True:
		selectStage(stage)
		inspectRepairReplace()	
		supply()
		battle(stage)

stages = { "7-4b" }