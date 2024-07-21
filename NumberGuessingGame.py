import random

print('Welcome to The Number Guessing Game')
user_input = input("Please type a number: ")

if user_input.isdigit():
    user_input = int(user_input)
    
elif user_input <= 0:
        print('Note that the Number should be greater than 0')
        quit()
else:
    print('Value should be a number')
    quit()

num_maker = random.randint(0, user_input)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == num_maker:
        print("You got it!")
        break
    elif user_guess > num_maker:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"Congrats! You got it in {guess} guesses")
