#start
def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def check_win(board, mark):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == mark for i in combo) for combo in win_combinations)

def tic_tac_toe():
    board = [str(i + 1) for i in range(9)]
    current_player = "X"
    while True:
        display_board(board)
        move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
        if board[move] not in "XO":
            board[move] = current_player
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif all(spot in "XO" for spot in board):
                display_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

while True:
    tic_tac_toe()
    if input("Do you want to play again? (yes/no): ").lower() != "yes":
        print("Goodbye!")
        break

