"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, Paper, Scissor)
2- Computer choice(Computer will choose randomly not conditionaly)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random
item_list = ["Rock", "Paper","Scissor", ]
user_choise = input("Enter your move = Rock, Paper, Scissor = ")

comp_choice = random.choice(item_list)

print(f"User choice = {user_choise}, Computer choice = {comp_choice}")

if user_choise == comp_choice:
    print("Both chooses same: Match Tie")

elif user_choise == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choise == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer win")
    else:
        print("Paper covers rock, You win")

elif user_choise == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")
        
            


    



