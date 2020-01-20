from stages import stages
import message
from monitor import *

def main():
	img = takeScreenshot()
	img.save("./stateImages/combatPreparationStatisticSquardron1.png")
	x = 956
	y = 500
	print((x,y),":",str(img.getdata()[y*1497+x])+",")

	# while True:
	# 	stage = input(message.enterStage)
	# 	if stage in stages:
	# 		stages[stage]()
	# 	else:
	# 		print(message.invaildStage)

if __name__== "__main__":
	main()