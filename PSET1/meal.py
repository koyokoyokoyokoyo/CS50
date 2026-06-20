#Meal time
def main():
    time = convert(input("Enter time: ").strip())
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(n):
    h, m = map(int, n.replace("a.m.","").replace("p.m.","").split(":")) #map used to turn all items to int
    if "p.m." in n and h != 12: # handles all of pm
        h += 12
    if "a.m." in n and h == 12:#handles midnight, no need for rest of arm, think abt it!
        h == 0
    return h + m / 60

if __name__ == "__main__":
    main()

#Adittional notes(lecture):
name = input("What's your name? ")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")