from custom_things import *

rps_choice_list = ['rock', 'paper', 'scissors']
ct_choice_list = ['heads', 'tails']

print_slow("""
Do you want to read the instructions?
""")
user_response = input("*Press Y if you do, otherwise enter any key: ")
print(section_line)
if user_response.upper() == 'Y':
    print_slow("""Instructions: Play against the computer in a game of rock paper scissors.
The winner gets to decide whether they want heads or tails.
The coin toss decides who ultimately wins.
""")

print_slow("What are the 2 choices you are deciding between?")
choice_1 = input("*Enter choice 1: ")
choice_2 = input("*Enter choice 2: ")
general_choice_list = [choice_1, choice_2]
player1_general_choice = choice(general_choice_list)
if player1_general_choice == choice_1:
    player2_general_choice = choice_2
elif player1_general_choice == choice_2:
    player2_general_choice = choice_1

print(section_line)

print_slow(f"You have been randomly assigned to play for {player1_general_choice}.")

print(section_line)

print_slow(f"{choice_1} or {choice_2}? Let's see which wins!\n")

while True:
    print_slow(f"Choose: rock, paper, or scissors?")
    while True:
        player1_rps_choice = input("*Enter choice: ")
        print(section_line)
        if player1_rps_choice.lower() == 'rock':
            print_slow("You have chosen rock.\n")
            break
        elif player1_rps_choice.lower() == 'paper':
            print_slow("You have chosen paper.\n")
            break
        elif player1_rps_choice.lower() == 'scissors':
            print_slow("You have chosen scissors.\n")
            break
        else:
            print_slow("Invalid response. Please type your choice: rock, paper, or scissors.")
        
    player2_rps_choice = choice(rps_choice_list)

    print_slow(f"""The computer has randomly chosen... {player2_rps_choice}!\n""")

    if (
        (player1_rps_choice.lower() == 'rock' and player2_rps_choice == 'scissors') or 
        (player1_rps_choice.lower() == 'paper' and player2_rps_choice == 'rock') or 
        (player1_rps_choice.lower() == 'scissors' and player2_rps_choice == 'paper')
    ):
        print_slow("You won!")
        player1_rps_winner = True
        break
    elif (
        (player1_rps_choice.lower() == 'rock' and player2_rps_choice == 'paper') or 
        (player1_rps_choice.lower() == 'paper' and player2_rps_choice == 'scissors') or 
        (player1_rps_choice.lower() == 'scissors' and player2_rps_choice == 'rock')
    ):
        print_slow("You lost!")
        player1_rps_winner = False
        break
    elif player1_rps_choice == player2_rps_choice:
        print_slow("You tied! Let's try that again.\n")
    
if player1_rps_winner == True:
    print_slow("But it's not over yet...\n")
elif player1_rps_winner == False:
    print_slow("But don't worry, you have another chance!\n")

print_slow("We're moving on to the coin toss.")

player2_ct_choice = choice(ct_choice_list)

if player1_rps_winner == True:
    print_slow("""Since you won, you get to choose whether you want heads or tails.
Which will it be?""")
    while True:
        player1_ct_choice = input('*Enter response: ')
        print(section_line)
        if player1_ct_choice.lower() == 'heads':
            print_slow("""You have chosen heads.
The computer will be tails.""")
            break
        elif player1_ct_choice.lower() == 'tails':
            print_slow("""You have chosen tails.
The computer will be heads.""")
            break
        else:
            print_slow("Invalid response. Type either heads or tails.")
elif player1_rps_winner == False:
    print_slow(f"""Since the computer won, it gets to choose whether it wants heads or tails.
And it has chosen... {player2_ct_choice}!""")
    if player2_ct_choice == 'heads':
        print_slow("You will be tails.")
        player1_ct_choice = 'tails'
    elif player2_ct_choice == 'tails':
        print_slow("You will be heads.")
        player1_ct_choice = 'heads'

print_slow("Let's do the coin toss now!")
ct_result = choice(ct_choice_list)
print_slow(f"And it's... {ct_result}!")

if ct_result == player1_ct_choice:
    print_slow(f"""Congratulations! You won!
{player1_general_choice} is the winner!""")
elif ct_result != player1_ct_choice:
    print_slow(f"""Unfortunately, you've lost.
{player2_general_choice} is the winner!""")

print_slow("Thanks for playing!")
