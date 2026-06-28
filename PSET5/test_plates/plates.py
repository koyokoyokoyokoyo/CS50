def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    dFlag = False
    if not s.isalnum():
        return False
    if not (2 <= len(s) <= 6):
        return False
    if not (s[:2]).isalpha():
        return False
    for c in s:
        if c.isdigit():
            if not dFlag:
                dFlag = True
                if c == '0':
                    return False
        if c.isalpha():
            if dFlag:
                return False
    return True

if __name__ == "__main__":
    main()