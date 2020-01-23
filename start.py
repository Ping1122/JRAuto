from StageManager import stageManager
from messageService import MessageService
from logger import log, Types

def main():
	stageManager = StageManager()
	while True:
		log(MessageService().enterStagePrompt(stageManager.stages), Types.info)
		stage = input()
		stageManager.levelStage(stage)

if __name__== "__main__":
	main()
