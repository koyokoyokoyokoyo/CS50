import re

def main():
    print(count(input("Text: ")))


def count(s):
    list = re.findall(r"\bum", s, re.IGNORECASE)
    count = len(list)
    list2 = re.findall(r"\Bum", s, re.IGNORECASE)
    if len(list2) > 0:
        return 0
    else:
        return count




if __name__ == "__main__":
    main()