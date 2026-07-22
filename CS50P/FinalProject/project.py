from pyfiglet import Figlet
from PIL import Image
import subprocess
from random_word import RandomWords
import random
import cowsay
import sys

lives = 7
r = RandomWords()
word = r.get_random_word()
scramble = ''.join(random.sample(word, len(word)))
#__________________________________________________________________
#PLAYS YOUR SOUND (IF USER HAS MP3 AUDIO!!!)/inserts image in new window
def play_audio_image():
    try:
        audioFile = "What's this!-(151k).mp3"
        p =subprocess.Popen(["afplay", audioFile])
    except KeyboardInterrupt:
        sys.exit()
    imageOutput = Image.open("thumbnail.jpg")
    imageOutput.show()
    return p
#__________________________________________________________________
#Opener
def starter():
    try:
        n = input("Start?[y/n] ")
        return n
    except Exception:
        raise Exception("You must enter y or n ")

#__________________________________________________________________
def input_control(g):
    global lives
    while True:
        userInput = input("Guess a letter: ")
        if userInput in g:
            if lives == 0:
                p.terminate()
                sys.exit("You lost.")
            print(f"You have already guessed that. Lost one life. {lives} remaining!!!")
        else:
            g.append(userInput)
            return userInput

#__________________________________________________________________

def Calculate():
    global lives
    scrambleNew = "_"*len(word) #A string consisting of _ _ _ etc..
    scrambleList = list(scrambleNew) # A list of the scarmbleNew
    wordList = list(word)
    userList = []

    while lives > 0:
        userInput = input_control(userList)
        if userInput not in wordList: #letter guessed isnt in the word
            lives -= 1 #Lost 1 life
            if lives == 0:
                p.terminate()
                figlet = Figlet(font='doh')
                print(figlet.renderText("You lost"))
                sys.exit()
            print(f"You lost 1 life! {lives} remaining!!!")
        else:
            for i in range(len(word)):
                if wordList[i] == userInput:
                    scrambleList[i] = userInput #set the correct position of said letter to it's "_" variant
        print(*scrambleList) #print current progress of _ _ _ etc..
        if scrambleList == wordList:
            figlet = Figlet(font='mini')
            print(figlet.renderText("You WON!!!!! I LOVE YOU!")) #You win. exits the loop!
            p.terminate()
            subprocess.Popen(["afplay", "cheer.mp3"])
            sys.exit()

#__________________________________________________________________
def main():
    global p
    #______________________________________________________________
    #Introductory Part
    figlet = Figlet(font='rev')
    p = play_audio_image() #starts the music
    #prints out name of program
    print(figlet.renderText("What's This!"))
    #introduction
    print("\nINTRODUCTION:\n\nThis is a game based on a guessing game that\nfrequently appeared in the show seitokai yakuindomo,"
    "\nexcept now you will be guessing a mystery word,"
    "\nwith 7 hearts before you lose.\nGood Luck !")
    #Outputs out image in another window!
    
    #______________________________________________________________
    #program begins
    try:
        startTrigger = starter()
    except Exception as e:
        print(e)
    if startTrigger.lower() == "y":
        figlet = Figlet(font='doom')
        #prints out name of program
        print(figlet.renderText("String Rearrangement!"))
        print("\nTry and decode what the linux penguin is saying ;O")
        cowsay.tux(f"{scramble}")
        Calculate()
    else:
        p.terminate()
        exit("Goodbye. ")

if __name__ == "__main__":
    main()
