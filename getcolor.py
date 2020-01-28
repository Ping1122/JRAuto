from components.monitor import Monitor

def main():
	
	x = []
	y = []
	for _ in range(4):
		x.append(int(input("x:")))
		y.append(int(input("y:")))
	img = Monitor().takeScreenshot()
	for i in range(4):
		print((x[i],y[i]),":",str(img.getdata()[y[i]*2558+x[i]])+",")

if __name__== "__main__":
	main()