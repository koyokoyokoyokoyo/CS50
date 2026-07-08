def main():
    #TUPLE replace
    student = get_student()
    if student[0] == "Padma":
        student[1] == "Ravenclaw"
    #if DICTIONARY REPLACE
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")
    #if DICTIONARY:
    print(f"{student['name']} from {student['house']}") #CANT USE double q. inside double q.
    #if CLASS
    print(f"{student.name} from {student.house}")
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     #tuple. You are returning 1 item with two things. (x, y)
#     return [name, house] #or you can return a tuple/list

# #Using a dictionary instead
# def get_student():
#     student = {}
#     student["name"] = input("Name: ") #name key, value of input
#     student["house"] = input("House: ")
#     return student
    #return {"name": name, "house": house} <- doesn't need a dictionary initialized before hand!
    #Now about classes! (You can read more about it in the documentation)

class Student: #constructor
    def __init__(self, name, house): #instance method. Initializes the contents of an object from a class
        #writing house=None for e.g means entering a value for house is OPTIONAL
        self.name = name #self.xxxx is an instance variable! Adds variable to instance object
        self.house = house #by not writing it as self._house, it assures that it goes through the setter, including a _ will circumvent this
    def __str__(self): # prints the class out in string format
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) #saying cls(..) instead of Student() allows the code to be flexible, and easily inherited

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property #THIS IS A GETTER (mandatory if u want to have a setter)
    def house(self):
        return self._house
    
    @house.setter #THIS IS A SETTER
    def house(self, house):
        if house not in ["Gryffindor", "HufflePuff", "RavenClaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = Student.get()
    print(student) #triggers __str__ method

#there exists @staticmethod too!
#instance methods/variables = specific objects
#class methods/variables = all objects of class