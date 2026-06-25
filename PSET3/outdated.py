list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = input("Date: ").strip()
    try:
        #input in MM-DD-YYYY
        if '/' in user_input:
            m, d, y = map(int, user_input.split('/'))
            #output in YYYY-MM-DD
            print(f"{y:02}", f"{m:02}", f"{d:02}", sep='-')
            break
        #input in MM-DD-YYYY
        elif ' ' in user_input:
            user_input = user_input.replace(",", "")
            m, d, y = user_input.split(' ')
            d, y = map(int, [d, y])
            m = list.index(m) + 1
            #output in YYYY-MM-DD
            print(f"{y:02}", f"{m:02}", f"{d:02}", sep='-')
            break
    except ValueError:
        pass
