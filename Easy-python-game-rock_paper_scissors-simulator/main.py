import random

print("Start game!")
list = ["rock", "paper", "scissors"]
winners = [("scissor", "paper"), ("paper", "rock"), ("rock", "scissors")]
round = 1
me = comp = 0
my_choice = input(f"Round {round}\nType your choice here (rock, paper or scissors): ")
while my_choice != '':
    comp_choice = random.choice(list)
    if my_choice == comp_choice:
        print(my_choice + " vs " + comp_choice + "\nIt's the draw!\n")
        me += 1
        comp += 1
    elif (my_choice, comp_choice) in winners:
        print(my_choice + " vs " + comp_choice + "\nYou Won!\n")
        me += 1
    else:
        print(my_choice + " vs " + comp_choice + "\nYou Lost!\n")
        comp += 1
    round += 1
    my_choice = input(f"Round {round}\nType your choice here (rock, paper or scissors): ")

print(f"Final score: YOU - {me} COMPUTER - {comp}")
