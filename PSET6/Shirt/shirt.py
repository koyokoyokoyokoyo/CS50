import sys
from PIL import Image, ImageOps
import os

fileInput = sys.argv[1] #user cmd-line input
fileOutput = sys.argv[2] #user cmd-line output

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many command-line argumnents")
    sys.exit()
elif len(sys.argv) == 3:
    temp1 = os.path.splitext(fileInput)
    temp2 = os.path.splitext(fileOutput)
    if not (temp1[1].lower() in ['.jpg','.jpeg','.png']) or not (temp2[1].lower() in ['.jpg','.jpeg','.png']):
        print("Invalid input")
        sys.exit()
    else:
        if not temp1[1] == temp2[1]:
            print("Input and Output have different extensions")
            sys.exit()

try:
    img = Image.open("before1.jpg")
    img2 = Image.open("shirt.png") #the SHIRT
    imgnew = ImageOps.fit(img, (600,600)) #muppet image
    imgnew.paste(img2, img2) #The first instance of img2 says that this is the image I want to place on top.
    #the second instance of img2 tells us that we want to use THAT as a mask(alpha band). LOOK at the documentation for reference!
    imgnew.save(f"{fileOutput}")
except FileNotFoundError:
    print("File not found :()")
    sys.exit()