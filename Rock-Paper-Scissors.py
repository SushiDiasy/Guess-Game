import random

player_wins = 0
sys_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors to play or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        print("Does not seem like a valid command...")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    sys_pick = choices[random_number]
    print("Computer picked", sys_pick + ".")

    if user_input == "rock" and sys_pick == "scissors":
        print("You won!")
        player_wins += 1

    elif user_input == "paper" and sys_pick == "rock":
        print("You won!")
        player_wins += 1

    elif user_input == "scissors" and sys_pick == "paper":
        print("You won!")
        player_wins += 1

    else:
        print("You lost!")
        sys_wins += 1

print("You won", player_wins, "times.")
print("The computer won", sys_wins, "times.")
print("Goodbye!")