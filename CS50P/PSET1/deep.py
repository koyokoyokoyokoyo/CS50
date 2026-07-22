#Deep
UserAnswer = input("What is the answer to the Great Question? ")
UserAnswer = UserAnswer.strip().lower()

if UserAnswer == "42" or UserAnswer == "fourty-two" or UserAnswer == "fourty two":
    print("Yes")
else:
    print("No")