from csv import DictReader
from csv import DictWriter
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

#Check for valid command-line inputs
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many command-line argumnents")
    sys.exit()
elif not filename1.endswith(".csv"):
    print(f"Could not read{filename1}")
    sys.exit()
    
names = []
try:
    with open(filename1, "r") as before, open(filename2, "w") as after:
        reader = DictReader(before)
        writer = DictWriter(after, fieldnames=["first","last","house"])
        writer.writeheader()
        

        for row in reader:
            last, first = row["name"].split(",")
            first = first.strip()
            writer.writerow(
                {
                    "first":first,
                    "last":last,
                    "house":row["house"]
                }
            )
except FileNotFoundError:
    print("File does not exist")