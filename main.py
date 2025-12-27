def print_board(board):
    """
    Prints the current state of the board.
    """
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_winner(board, player):
    """
    Checks if the specified player has won.
    Returns True if won, False otherwise.
    """
    # All possible winning combinations (rows, cols, diagonals)
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for a, b, c in win_conditions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


def is_board_full(board):
    """
    Checks if there are no empty spots left.
    """
    return all(spot in ['X', 'O'] for spot in board)


def play_game():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 'X'

    print("--- Tic Tac Toe ---")
    print_board(board)

    while True:
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): "))

            # Validate input range
            if choice < 1 or choice > 9:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue

            # Check if spot is taken
            if board[choice - 1] in ['X', 'O']:
                print("That spot is already taken! Try again.")
                continue

            # Update board
            board[choice - 1] = current_player
            print_board(board)

            # Check for Win
            if check_winner(board, current_player):
                print(f"Congratulations! Player {current_player} wins!")
                break

            # Check for Tie
            if is_board_full(board):
                print("It's a tie!")
                break

            # Switch Player
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        play_game()
        replay = input("Play again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()