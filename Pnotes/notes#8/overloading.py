class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0): #gives them a defualt vlaue of 0
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    #operator overloading
    #object.__add__(self, other)
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
weasley = Vault(25, 50, 100)
#note: you CAN add values from two seperate classes per say

total = potter + weasley
print(total)