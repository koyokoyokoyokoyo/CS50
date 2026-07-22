import validators

def main():
    print(validator(input("What's your email? ")))

def validator(c):
    if validators.email(c):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()