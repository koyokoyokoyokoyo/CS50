import random

class Hat:
    houses = ["Gryffindor", "HufflePuff", "RavenClaw", "Slytherin"]#just a vairable inside of the class. Accessible by all methods in class

    @classmethod
    #there exists no other thing like @instancemethod, a method is auto defined as an instance method
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses)) #houses is now a class variable, not a instance variable! :)


Hat.sort("Harry")