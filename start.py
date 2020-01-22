from taskManager import TaskManager
import message
from logger import *

def main():
	taskManager = TaskManager()
	while True:
		log(message.enterStage, Types.info)
		stage = input()
		taskManager.levelStage(stage)

if __name__== "__main__":
	main()
