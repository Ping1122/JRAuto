from components.monitor import Monitor
from data.constants import IMG_RESOLUTION 

def main():
	
	img = Monitor().takeScreenshot()
	data = list(img.getdata())
	target = {
		(2027, 1280) : ((74, 61, 89, 255), ),
		(2371, 1137) : (72, 72, 72, 255),
		(2016, 1238) : (255, 246, 226, 255),
		(1700, 1290) : (55, 134, 208, 255),
	}
	minKey = min(key[1]*IMG_RESOLUTION[0]+key[0] for key in target.keys())
	pattern = dict()
	for key, value in target.items():
		pattern[key[1]*IMG_RESOLUTION[0]+key[0]-minKey] = value
	maxKey = max(pattern.keys())
	for i in range(len(data)-maxKey):
		if all(data[i+key] == value for key, value in pattern.items()):
			x = i % IMG_RESOLUTION[0]
			y = i // IMG_RESOLUTION[0]
			print(x,y)

if __name__== "__main__":
	main()