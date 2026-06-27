import random
def main():
    while True:
        try:
            userChoice = int(input("Level: "))
            answer = random.randint(1, userChoice)
        except ValueError:
            pass
        else:
            userGuess = int(input("Guess: "))
            if userGuess > answer:
                print("Too large!")
            elif userGuess < answer:
                print("Too small!")
            else:
                print("Just Right!")
                break
if __name__ == "__main__":
    main()