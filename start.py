from stages import *
import message
from logger import *

def main():
	while True:
		log(message.enterStage, Types.info)
		stage = input()
		startStage(stage)

if __name__== "__main__":
	main()