def main():
    while True:
        try:
            userInput = convert(input("Fraction: "))
            answer = gauge(userInput)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(answer)


def convert(userInput):
    x, y = map(int, userInput.split("/"))
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    percent = (x/y) * 100
    return round(percent, 0)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()