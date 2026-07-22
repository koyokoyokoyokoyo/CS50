def main():
    answer = convert()
    print(answer)

def convert():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = map(int, fraction.split("/"))
            if x > y:
                raise ValueError
            percentage = (x/y) * 100
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{x/y:.0%}"
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()