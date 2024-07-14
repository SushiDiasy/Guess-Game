print(" Hello! Welcome to a terminal quiz! ")

Name = input(" What would you like your player name to be? ")
startgameques = input(f"Hey {Name}, Do you want to play? ")

if startgameques.lower() != "yes":
    quit()
elif startgameques.lower() != "no":
    print("Let's dive in! ")

score = 0
quesnum = 0
worldspec = input("What does Nvidia produce? ")
if compspec.lower() == "graphic cards":
    print('Right!')
    score += 1
    quesnum += 1
else:
    print("Wrong!")
    quesnum += 1

answer = input("What does HDD stand for? ")
if answer.lower() == "hard drive":
    print('Right!')
    score += 1
    quesnum += 1
else:
    print("Wrong")
    quesnum += 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Right!')
    score += 1
    quesnum += 1
else:
    print("Wrong!")
    quesnum += 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Right')
    score += 1
    quesnum += 1
else:
    print("Wrong")
    quesnum += 1

print("You got " + str(score) + " questions correct out of " + str(quesnum) + "!")
print("You got " + str((score / 4) * 100) + "%.")