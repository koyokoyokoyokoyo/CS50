def main():
    userInput, output = input("Input: "), ""
    for c in userInput:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            c = ''
        output += c
    print("Output:",output)

if __name__ == "__main__":
    main()