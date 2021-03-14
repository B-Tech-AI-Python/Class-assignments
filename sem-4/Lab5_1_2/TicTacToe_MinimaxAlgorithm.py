import numpy as np
from math import inf as infinity

def play_move(state, player, block_num):
    """Method for checking the correct move on Tic-Tac-Toe."""

    # Assign the player move on the current position of Tic-Tac-Toe if condition is True
    if state[int((block_num-1)/3)][int((block_num-1)%3)] == ' ':
        state[int((block_num-1)/3)][int((block_num-1)%3)] = player

    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        play_move(state, player, block_num)


def copy_game_state(state):
    """Method to copy the current game state to new_state of Tic-Tac-Toe."""

    new_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state


def check_current_state(game_state):
    """Method to check the current state of the Tic-Tac-Toe."""

    # Check horizontals in first row
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] != ' '):
        return game_state[0][0], "Done"
    # Check horizontals in second row
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] != ' '):
        return game_state[1][0], "Done"
    # Check horizontals in third row
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] != ' '):
        return game_state[2][0], "Done"
    
    # Check verticals in first column
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] != ' '):
        return game_state[0][0], "Done"
    # Check verticals in second column
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] != ' '):
        return game_state[0][1], "Done"
    # Check verticals in third column
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] != ' '):
        return game_state[0][2], "Done"
    
    # Check left diagonal
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] != ' '):
        return game_state[1][1], "Done"
    # Check right diagonal
    if (game_state[0][2] == game_state[1][1] and game_state[1][1] == game_state[2][0] and game_state[0][2] != ' '):
        return game_state[1][1], "Done"

    # Set the draw_flag to 0
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == ' ':
                draw_flag = 1

    if draw_flag == 0:
        return None, "Draw"

    return None, "Not Done"


def print_board(game_state):
    """Method to print the Tic-Tac-Toe Board."""

    print('----------------')
    print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |')
    print('----------------')


def getBestMove(state, player):
    """Method for implement the Minimax Algorithm."""

    # check if winner
    winner_loser, done = check_current_state(state)

    if done == "Done" and winner_loser == 'O':
        return 1
    elif done == "Done" and winner_loser == 'X':
        return -1
    elif done == "Draw":    
        return 0

    moves = []
    empty_cells = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                empty_cells.append(i*3 + (j+1))

    # Iterate over all the empty_cells
    for empty_cell in empty_cells:
        move = {}

        move['index'] = empty_cell

        new_state = copy_game_state(state)

        play_move(new_state, player, empty_cell)

        # if player is computer
        if player == 'O':
            # Call getBestMove method with new_state and human player ('X')
            # to make more depth tree for human
            result = getBestMove(new_state, 'X')
            move['score'] = result
        else:
            # Call getBestMove method with new_state and computer player('O')
            # to make more depth tree for computer
            result = getBestMove(new_state, 'O')
            move['score'] = result

        moves.append(move)

    # Find best move
    best_move = None

    # Check if player is computer('O')
    if player == 'O':
        best = -infinity

        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']

    return best_move


# Now PLaying the Tic-Tac-Toe Game
play_again = 'Y'

# Create the Two Players as 'X'/'O'
players = ['X','O']

while play_again == 'Y':
    # Set the empty board for Tic-Tac-Toe
    game_state = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]

    # Set current_state as "Not Done"
    current_state = "Not Done"
    print("\nNew Game!")
    
    # Print the game_state 
    print_board(game_state)
    
    # Select the player_choice to start the game
    player_choice = input("Choose which player goes first - X (You) or O(Computer): ").lower()
    
    # Set winner as None
    winner = None

    # If player_choice is 'x' for humans else for computer
    if player_choice == 'x':
        # Set current_player_idx is 0
        current_player_idx = 0
    else:
        # Set current_player_idx is 1
        current_player_idx = 1

    while current_state == "Not Done":
        # Human Turn
        if current_player_idx == 0: 
            block_choice = int(input("Your turn please! Choose where to place (1 to 9): "))
            play_move(game_state, players[current_player_idx], block_choice)

        # Computer turn
        else:
            block_choice = getBestMove(game_state, players[current_player_idx])
            play_move(game_state, players[current_player_idx], block_choice)
            print("AI plays move: " + str(block_choice))

        print_board(game_state)

        winner, current_state = check_current_state(game_state)
        if winner != None:
            print(str(winner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1) % 2

        if current_state == "Draw":
            print("Draw!")

    play_again = input('Wanna try again?(Y/N): ').upper()
    if play_again == 'N':
        print('Thank you for playing Tic-Tac-Toe Game!!!!!!!')
