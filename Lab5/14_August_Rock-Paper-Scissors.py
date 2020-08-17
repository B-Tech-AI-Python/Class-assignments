"""
This is a program to simulate the game of "Rock-Paper-Scissors" using python.

This program uses the 'random' module when the player wants to play against the computer.
"""
import random


def replay():
    """Gives the user the otion to play again."""
    res = input('Do you want to play again? Enter Yes or No:')
    return res.lower().startswith('y')


options = ['Rock', 'Paper', 'Scissors']


def option():
    while True:
        try:
            choice = input("What would you like to choose? Rock, Paper or Scissors: ")
            choice = choice.lower()
            if choice.startswith('r'):
                return options[0]
            elif choice.startswith('p'):
                return options[1]
            elif choice.startswith('s'):
                return options[2]
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")


while True:
    try:
        players = int(input("How many players? 1 or 2: "))
        if isinstance(players, int):
            if players == 1:
                player1_choice = option()
                computer = options[random.randint(0, 2)]
                player2_choice = "not playing"
                break
            elif players == 2:
                player1_choice = option()
                player2_choice = option()
                computer = "not playing"
                break
            else:
                print("Choose 1 or 2!")
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("Invalid input! Try Again!")

# win check
if player1_choice == computer or player1_choice == player2_choice:
    print("Tie!")

# rock
elif player1_choice == "Rock":
    if computer == "Paper":
        print("Computer wins!", computer, "covers", player1_choice)

    elif player2_choice == "Paper":
        print("Player 2 wins!", player2_choice, "covers", player1_choice)

    else:
        print("Player 1 wins!", player1_choice, "smashes", computer)

# paper
elif player1_choice == "Paper":
    if computer == "Scissors":
        print("Computer wins!", computer, "cut", player1_choice)

    elif player2_choice == "Scissors":
        print("Player 2 wins!", player2_choice, "cut", player1_choice)

    else:
        print("Player 1 wins!", player1_choice, "covers", computer)

# scissors
elif player1_choice == "Scissors":
    if computer == "Rock":
        print("Computer wins", computer, "smashes", player1_choice)

    elif player2_choice == "Rock":
        print("Player 2 wins!", player2_choice, "smashes", player1_choice)

    else:
        print("Player 1 wins!", player1_choice, "cut", computer)
