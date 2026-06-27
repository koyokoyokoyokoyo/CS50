def main():
    list = {}
    while True:
        try:
            shopping = input().upper()
            #check if there
            if shopping in list:
                list[shopping] += 1
            #if not
            else:
                list.setdefault(shopping, 1)
        #to detect ctrl d
        except EOFError:
            #sorting alphabetically
            for grocery in sorted(list):
                print(list[grocery], grocery)
            break

if __name__ == "__main__":
    main()