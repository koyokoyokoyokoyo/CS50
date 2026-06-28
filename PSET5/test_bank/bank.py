def main():
    greeting = input("Greeting: ").strip().lower()
    print(bank(greeting))

def bank(m):
    if m.startswith("hello"):
        return "$0"
    elif m.startswith("h"):
        return "$20"
    else:
        return "$100"