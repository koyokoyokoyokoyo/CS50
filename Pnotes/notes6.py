import csv #library to help w/ reading CSV files
#checkour pillow library. helps with image files

name = input("What's your name? ")
with open("names.txt", "r") as file:
    #file.write(f"{name}\n")
    lines = file.readlines() # when using "r" read mode

for line in lines:
    print("hello,",line.rstrip()) #.strip to get rid of the extra new lines we added when writing. rstrip == RIGHT ONLY strip

#for an easier method when reading, without having to read all of the lines first:
#by default, opening a file opens it in read mode, meainng u don't rly have to specify "r"
names = []
with open("names.txt") as file:
    for line in file:
        #print("hello,", line.rstrip())
        names.append(line.rstrip())

for n in sorted(names):
    print(f"hello,", {n})

###code names.csv <-- this creats a txt file where you can seperate values with commas
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
#Dictionary in list
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"], reverse=True): #lambda = function with no name
#THE FIRST STUDENT IN LAMBDA IS JUST A PARAMETER AND WE ^^ CAN CALL IT WHATEVER WE WANT TO!
    print(f"{student['name']} is in {student['house']}")

#using the csv library(don't forget to import csv)
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader: #this sorts out all the commas and what not for you, saving you the hastle
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")

#you can use csv.DictReader when adding column names to your csv file
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]}) #you can also just write students.append(row)
#this way your headers/column names are more flexible; despite changes to the header(in csv file)
#REMEMBER A READER RETURNS A LIST, WHEREAS A DICTREADER RETURNS A DICTIONARY

#csv writing
name = input("wat's ur name: ")
house = input("wat house? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home]) #remember, a LIST!!

#using DictWriter
name = input("wat's ur name: ")
house = input("wat house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["names", "home"]) #fieldnames is an argument to show it wat/how our column headers are
    writer.writerow({"name": name, "home": home})#we could've written "home" then "name"
                                                 #it doesn't matter, bcz fieldnames is there to show how our headers are set

#_________________________________IMAGE FILE_______________________________________________________
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg) #Image.open() is from the pillow library
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0 #writes an image directly onto your local storage
    #               ^^save all frames                         ^^200ms       ^^ 0 == loops an infinite nmbr of times
)
#after successfully running python customes.py costume1.py costume2.py
#> code costumes.gif