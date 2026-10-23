import random

opts = ["rock", "paper", "scissors"]
user_opt = int(input("Choose 0 for rock, 1 for paper, and 2 for scissors: "))
user_played = opts[user_opt]
machine_opt = random.randint(0, 2)
machine_played = opts[machine_opt]

if user_played == "rock":
    if machine_played == "rock":
        print("Machine played rock, its a draw!")
    elif machine_played == "paper":
        print("Machine played paper, you lose!")
    else:
        print("Machine played scissors, you win!!!")

elif user_played == "paper":
    if machine_played == "rock":
        print("Machine played rock, you win!!!")
    elif machine_played == "paper":
        print("Machine played paper, its a draw!")
    else:
        print("Machine played scissors, you lose!")

else:
    if machine_played == "rock":
        print("Machine played rock, you lose!")
    elif machine_played == "paper":
        print("Machine played paper, you win!!!")
    else:
        print("Machine played scissors, its a draw!")