from stages import stages
import message
from monitor import *

def main():
	while True:
		stage = input(message.enterStage)
		if stage in stages:
			stages[stage]()
		else:
			print(message.invaildStage)

if __name__== "__main__":
	main()