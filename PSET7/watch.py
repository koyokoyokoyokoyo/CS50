import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    listt = (re.findall(r"\bhttps?://(?:www.)?youtube.com/embed/[a-zA-Z0-9]{11}\b", s))
    if listt == "":
        return None
    else:
        return listt[0]



if __name__ == "__main__":
    main()