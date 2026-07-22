def main():
    answer = input("Input: ")
    print("Output:",twitter(answer))

def twitter(userInput):
    output = ""
    for c in userInput:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            c = ''
        output += c
    return output

if __name__ == "__main__":
    main()