# ============================================================
# TIC-TAC-TOE
# A two-player game played in the terminal.
# Players take turns choosing a position (1-9) on the board.
# The first player to get 3 in a row wins!
# ============================================================

# This list represents the 9 squares of the board.
# We use positions 1-9 (index 0 is unused so numbers match naturally).
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    # This function prints the current state of the board.
    # Each row shows 3 squares separated by vertical bars.
    print("\n " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print()

def check_winner(player):
    # This function checks if a given player ("X" or "O") has won.
    # It checks all 8 possible winning combinations (3 rows, 3 columns, 2 diagonals).

    # Check the three rows
    if board[1] == board[2] == board[3] == player:
        return True
    if board[4] == board[5] == board[6] == player:
        return True
    if board[7] == board[8] == board[9] == player:
        return True

    # Check the three columns
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    if board[3] == board[6] == board[9] == player:
        return True

    # Check the two diagonals
    if board[1] == board[5] == board[9] == player:
        return True
    if board[3] == board[5] == board[7] == player:
        return True

    # If none of the above matched, this player has not won yet
    return False

def check_draw():
    # If no square is empty (" "), it's a draw
    for i in range(1, 10):
        if board[i] == " ":
            return False  # Found an empty square, so the game is not a draw
    return True  # No empty squares found, it's a draw

def play_game():
    # This function runs the main game loop.
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9, left to right, top to bottom.")
    print_board()

    # We use a variable to track whose turn it is: "X" always goes first
    current_player = "X"

    # The game continues until someone wins or it's a draw
    while True:
        # Ask the current player to choose a position
        print("Player " + current_player + ", choose a position (1-9): ", end="")
        move = input()

        # Check if the input is a valid number between 1 and 9
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input! Please enter a number from 1 to 9.")
            continue  # Skip back to the top of the loop and ask again

        # Convert the input from text to an integer
        move = int(move)

        # Check if the chosen square is already taken
        if board[move] != " ":
            print("That square is already taken! Choose another.")
            continue  # Skip back to the top of the loop and ask again

        # Place the player's mark on the board
        board[move] = current_player

        # Print the updated board
        print_board()

        # Check if the current player has won
        if check_winner(current_player):
            print("Congratulations! Player " + current_player + " wins!")
            break  # Exit the loop, game is over

        # Check if the game is a draw
        if check_draw():
            print("It's a draw! No one wins.")
            break  # Exit the loop, game is over

        # Switch to the other player for the next turn
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Start the game
play_game()
