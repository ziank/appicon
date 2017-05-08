#/usr/bin/python
import sys
import os
from PIL import Image

def main(imagePath):
	image = Image.open(imagePath)
	retImage = image.resize((29, 29))
	retImage.save("29.png")
	retImage = image.resize((58, 58))
	retImage.save("29@2x.png")
	retImage = image.resize((87, 87))
	retImage.save("29@3x.png")

	retImage = image.resize((40, 40))
	retImage.save("40.png")
	retImage = image.resize((80, 80))
	retImage.save("40@2x.png")
	retImage = image.resize((120, 120))
	retImage.save("40@3x.png")
	retImage.save("60@2x.png")

	retImage = image.resize((180, 180))
	retImage.save("60@3x.png")

	retImage = image.resize((76, 76))
	retImage.save("76.png")
	retImage = image.resize((152, 152))
	retImage.save("76@2x.png")

	retImage = image.resize((167, 167))
	retImage.save("83.5@2x.png")


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Please use python AppIcon.py [imageName]!")
		exit()
	main(sys.argv[1])