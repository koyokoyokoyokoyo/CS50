#making faces
def main():
    userinput = input(("Enter input son: "))
    result = convert(userinput)
    print(result)

def convert(x):
    return x.replace(':(','🙁').replace(':)','🙂')
main()