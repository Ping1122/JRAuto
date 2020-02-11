from controllers.taskController import TaskController
from util.messages import Messages
from util.logger import log, Types

def main():
	taskController = TaskController()
	stageNum = 0
	while True:
		try:
			log(Messages().enterStagePrompt(), Types.info)
			stageNum = int(input())
		except:
			log(Messages().invalidUserInput(stageNum), Types.info)
			continue
		taskController.startTask(stageNum)
		
if __name__== "__main__":
	main()
