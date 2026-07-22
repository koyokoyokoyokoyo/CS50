from csv import DictReader
import sys
from tabulate import tabulate
#print(tabulate(table, headers, tablefmt="grid")) <-- FOR TABLE SHAPE

def main():
    #Check for valid command-line inputs
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line argumnents")
        sys.exit()
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit()
    try:
        with open(sys.argv[1]) as file:
            reader = DictReader(file)
            table = tabulate(reader, headers="keys", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()