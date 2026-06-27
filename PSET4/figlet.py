#importing libraries
import sys
import random
from pyfiglet import Figlet
def main():
    f = Figlet()

    #zero arguments
    if len(sys.argv) == 1:
        userInput = input("Input: ")
        randomFont = random.choice(f.getFonts())
        f.setFont(font=randomFont)
        print("Output:\n",f.renderText(f"{userInput}"))
    #two arguments
    elif len(sys.argv) == 3:
        #invalid syntax
        if sys.argv[1] not in ("-f", "--font"): #I used tuple, though this was through looking things up. I could've used:
        #if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("invalid command")
        else:
            if sys.argv[2] in f.getFonts():
                userInput = input("Input: ")
                userFont = f"{sys.argv[2]}"
                f.setFont(font=userFont)
                print("Output:\n",f.renderText(f"{userInput}"))
            else:
                sys.exit("invalid font")
if __name__ == "__main__":
    main()