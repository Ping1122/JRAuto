from components.monitor import Monitor

def main():
	img = Monitor().takeScreenshot()
	x = int(input("x:"))
	y = int(input("y:"))
	print((x,y),":",str(img.getdata()[y*1497+x])+",")

if __name__== "__main__":
	main()
