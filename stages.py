from actions import *
from logger import *
import message

def startStage(stage):
	if stage not in stages:
		log(message.invaildStage, Types.warning)
		return
	updateScreenshotAndState()
	count = 0
	while True:
		selectStage(stage)
		inspectRepairReplace()	
		supply()
		battle(stage)
		count += 1
		log("Complete " + stage + " for " + str(count) + " times", Types.info)

stages = { "7-1a", "7-4b" }