#Deep
UserAnswer = input("What is the answer to the Great Question? ")
UserAnswer = UserAnswer.strip().lower()

if UserAnswer == "42" or UserAnswer == "fourty-two" or UserAnswer == "fourty two":
    print("Yes")
else:
    print("No")

#Bank
Greeting = input("Greeting: ").strip().lower()

if Greeting.startswith("hello"):
    print("$0")
elif Greeting.startswith("h"):
    print("$20")
else:
    print("$100")

#Extensions
file = input("File Name: ").strip().lower().split('.')

if file[-1] == 'gif':
    print("image/gif")
elif file[-1] == 'jpg' or file[-1] == 'jpeg':
    print("image/jpeg")
elif file[-1] == 'png':
    print("image/png")
elif file[-1] == 'pdf':
    print("image/pdf")
elif file[-1] == 'txt':
    print("image/txt")
elif file[-1] == 'zip':
    print("image/zip")
else:
    print("application/octet-stream")

#Math Interperter

x, y, z = input("Enter xyz: ").strip().split() #this is called unpacking
x, z = int(x), int(z) #THIS IS ALSO UNPACKING, fairly explainable. used to enforce int onto x, z. for y it is impossible(its a symbol)
answer = eval(f"{x}{y}{z}") #THIS IS A USEFUL FUNCTION TO KNOW
print(f"{answer:.1f}")

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
    h, m = map(int, n.replace("a.m.","").replace("p.m.","").split(":"))
    if "p.m." in n and h != 12: # handles all of pm
        h += 12
    if "a.m." in n and h == 12:#handles midnight, no need for rest of arm, think abt it!
        h == 0
    return h + m / 60

if __name__ == "__main":
    main()