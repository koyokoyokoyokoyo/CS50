import sys

def main():
    count = 0
    filename = sys.argv[1]
    #Check for valid command-line inputs
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line argumnents")
        sys.exit()
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit()
    
    filename = sys.argv[1]
    try:
        with open(filename) as f:
            #checking for lines
            for line in f:
                if not line.lstrip().startswith("#") or not line.isspace():
                    count += 1
    
        print(count)
    #open() error incase file does not exist
    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()