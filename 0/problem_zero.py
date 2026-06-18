#PROBLEM SET 0
#indoor voice(#1)
userinput = input("Enter input please: ").lower()
print(userinput)
#playbackspeed
userinput = input("Enter input please: ").replace(' ','...')
print(userinput)
#making faces
def main():
    userinput = input(("Enter input son: "))
    result = convert(userinput)
    print(result)

def convert(x):
    return x.replace(':(','🙁').replace(':)','🙂')
#main()
#einstein
usermass = int(input("Enter mass: "))
userC = 300000000
total = userC * usermass
print("As per E=mc^2, the total E is:",total,"J")
#TipCalculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.removeprefix("$")
    d = float(d)
    return d


def percent_to_float(p):
    p = p.removesuffix("%")
    p = float(p)
    p = p / 100
    return p


main()