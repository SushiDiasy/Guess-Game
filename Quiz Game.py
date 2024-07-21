#SA

print("Hello! Welcome to a terminal quiz! ")

startgameques = input("Would you like to play?")

if startgameques.lower() == "no":
    quit()
elif startgameques.lower() == "yesYe":
    name = input("What would you like your player name to be? ")
    print(f"Okay {name}, Let's dive in!")

score = 0
quesnum = 0
worldspec = input("What does Nvidia produce? ")
if worldspec.lower() == "graphic cards":
    print('Right!')
    score += 1
    quesnum += 1
else:
    print("Wrong!")
    quesnum += 1

worldspec2 = input("What does HDD stand for? ")
if worldspec2.lower() == "hard drive":
    print('Right!')
    score += 1
    quesnum += 1
else:
    print("Wrong")
    quesnum += 1

worldspec3 = input("What does RAM stand for? ")
if worldspec3.lower() == "random access memory":
    print('Right!')
    score += 1
    quesnum += 1
else:
    print("Wrong!")
    quesnum += 1

worldspec4 = input("What does PSU stand for? ")
if worldspec4.lower() == "power supply":
    print('Right')
    score += 1
    quesnum += 1
else:
    print("Wrong")
    quesnum += 1

print(f"You got {str(score)} questions correct out of {str(quesnum)}!")
print(f"You got {str((score / 4) * 100)}%.")
