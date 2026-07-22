#Math Interperter
x, y, z = input("Enter xyz: ").strip().split() #this is called unpacking
x, z = int(x), int(z) #THIS IS ALSO UNPACKING, fairly explainable. used to enforce int onto x, z. for y it is impossible(its a symbol)
answer = eval(f"{x}{y}{z}") #THIS IS A USEFUL FUNCTION TO KNOW
print(f"{answer:.1f}")