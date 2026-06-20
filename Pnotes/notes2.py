def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow\n", end='') #removes extra space
# again, review print(*objects, sep=' ', end='\n', file=None, flush=False)

# students = ["H","L","A"]
# for i in range(len(students)):
#     print(i + 1, students[i], sep='-')

#DICTIONARY
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrir"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=', ')

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#" * size)