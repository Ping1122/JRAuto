from PIL import Image, ImageGrab
from states import *
from config import *
from util import *
from dangers import *

def analyzeState(img):
	imgData = img.getdata()
	for state, signature in stateSignature.items():
		if all(
			imgData[pixelPostionToImageDataIndex(pos)] == color
			for pos, color in signature.items()
		):
			return state
	return States.unknown
	
# def debug(state, imgData, pos, color):
# 	if state == States.sailingOffExpidition:
# 		print(imgData[pixelPostionToImageDataIndex(pos)], color)
# 	return 

def findDamagedShips(img):
	imgData = img.getdata()
	damagedShips = []
	for ship, signature in normalSignature.items():
		if all(
			imgData[pixelPostionToImageDataIndex(pos)] != color
			for pos, color in signature.items()
		):
			damagedShips.append(ship)
	return damagedShips

def checkStage74bExistsSubmarine(img):
	imgData = img.getdata()
	return all(
		imgData[pixelPostionToImageDataIndex(pos)] == color 
		for pos, color in stage74bExistsSubmarineSignature.items()
	)


def takeScreenshot():
	img = ImageGrab.grab(bbox = SIMULATOR_WINDOW_POSITION)
	return img
