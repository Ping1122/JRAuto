from controllers.gameController import GameController
from util.messages import Messages
from util.logger import log, Types

def main():
	gameController = GameController()
	stageNum = 0
	while True:
		try:
			log(Messages().enterStagePrompt(gameController.stages), Types.info)
			stageNum = int(input())
		except:
			log(Messages().invalidUserInput(stageNum), Types.info)
			continue
		gameController.levelStage(stageNum)
if __name__== "__main__":
	main()
