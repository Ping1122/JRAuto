from stages import stages
import message
from monitor import *

def main():
	img = takeScreenshot()
	print(analyzeState(img))

if __name__== "__main__":
	main()