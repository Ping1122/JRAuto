from components.monitor import Monitor


def main():
	
	img = Monitor().takeScreenshot()
	width = img.size[0]
	data = list(img.getdata())
	target = {
		(483, 466) : ((214, 97, 90), ),
		(547, 485) : ((173, 186, 189), ),
		(561, 470) : ((99, 69, 90), ),
		(615, 437) : ((24, 28, 24), ),
	}
	minKey = min(key[1]*width+key[0] for key in target.keys())
	pattern = dict()
	for key, value in target.items():
		pattern[key[1]*width+key[0]-minKey] = value
	maxKey = max(pattern.keys())
	for i in range(len(data)-maxKey):
		if all(data[i+key] == value for key, value in pattern.items()):
			x = i % width
			y = i // width
			print(x,y)

if __name__== "__main__":
	main()