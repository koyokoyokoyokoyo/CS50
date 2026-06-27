import inflect
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            userInput = input("Name: ")
            names.append(userInput)
        #detecting ctrl-d
        except EOFError:
            print("Adieu,adieu, to",p.join((names), sep=', and', sep_spaced=True, conj=''))
            break
if __name__ == "__main__":
    main()