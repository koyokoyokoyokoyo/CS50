import re

def main():
    print(validate(input("IPv4 Adress: ")))

def validate(ip):
    if matches := re.search(r"^(([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-1]?[0-9]?[0-9]|2[0-5][0-4]|25[0-5])$", ip):
        return True

if __name__ == "__main__":
    main()