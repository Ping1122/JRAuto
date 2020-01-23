from ..controller.stageManager import StageManager
from ..util.messages import Messages
from ..util.logger import log, Types

def main():
	stageManager = StageManager()
	while True:
		try:
			log(Messages().enterStagePrompt(stageManager.stages), Types.info)
			stageNum = int(input())
			stageManager.levelStage(stageNum)
		except:
			log(Messages().invalidUserInput(stageNum), Types.info)

if __name__== "__main__":
	main()
