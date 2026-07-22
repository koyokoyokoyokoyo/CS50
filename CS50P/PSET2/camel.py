def main():
    snake_case = ""
    camelCase = input("camelCase: ")
    for c in camelCase:
        if c.isupper() == True:
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    print("snake_case:",snake_case)
main()