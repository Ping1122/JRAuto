from stages import stages
import message
from monitor import *

def main():
	img = takeScreenshot()
	img.save("./stateImages/selectFormation.png")
	x = int(input("x:"))
	y = int(input("y:"))
	print((x,y),":",str(img.getdata()[y*1497+x])+",")

if __name__== "__main__":
	main()