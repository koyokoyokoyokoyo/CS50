def main():
    change, insert = 50, 0
    while change > insert:
        print("Amount Due: ", change - insert)
        coin = int(input("Insert Coin: "))
        if coin in [5,10,25]:
            insert += coin
    print("Change Owed:", insert - change)

if __name__ == "__main__":
    main()