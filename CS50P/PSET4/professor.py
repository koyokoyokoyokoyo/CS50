import random

def main():
    xlist = []
    ylist = []

    right, total = 0, 0
    level = get_level()
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        xlist.append(x)
        ylist.append(y)
        correct = xlist[i] + ylist[i]
        for j in range(3):
            try:
                userQuestion = int(input(f"{xlist[i]} + {ylist[i]} = "))
            except ValueError:
                pass
            if userQuestion == correct:
                right += 1
                break
            else:
                print("EEE")
                if j == 2:
                    print((f"{xlist[i]} + {ylist[i]} = {correct}"))
        total += 1
    print("Score: ",right)


def get_level():
    try:
        level = int(input("level: "))
    except ValueError:
        pass
    if level in (1,2,3):
        return level

def generate_integer(level):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)
        case _:
            raise ValueError("not part of available range.")

if __name__ == "__main__":
    main()