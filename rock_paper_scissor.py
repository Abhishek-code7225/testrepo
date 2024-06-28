# random used to get random number from python between two numbers
import random

Rock = 1
Paper = 2
Secissor = 3
close_game = True

while close_game:
    my_choice = int(input("Enter choice :- "))
    system_choice = random.randint(2, 3)

    while my_choice == system_choice:
        system_choice = random.randint(2, 3)
    if system_choice==2:
        print("system choice is Paper")
    if system_choice == 3:
        print("system choice is Secissor")
    if not my_choice in [1, 2]:
        print('please select another choice')
        break
    if my_choice == 1 and system_choice==2:
        winner = 'Paper wins'
    elif my_choice == 1 and system_choice==3:
        winner = 'Rock wins'
    elif my_choice == 2 and system_choice == 3:
        winner = 'Secissor wins' 
    print(winner)

    my_input = str(input("Want to play again then please type 'yes'."))

    if not my_input.lower() == 'yes':
        close_game = False