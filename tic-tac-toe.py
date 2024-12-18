import math

# Constants for the game
EMPTY = ' '
PLAYER_X = 'X'  # AI player
PLAYER_O = 'O'  # Human player

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the game is over
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row check
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column check
            return True
    if all([board[i][i] == player for i in range(3)]):  # Diagonal check
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Anti-diagonal check
        return True
    return False

# Function to check if the board is full (i.e., it's a draw)
def is_draw(board):
    return all([cell != EMPTY for row in board for cell in row])

# Minimax algorithm to evaluate the board
def minimax(board, depth, is_maximizing, alpha, beta):
    # Check for terminal states
    if is_winner(board, PLAYER_X):
        return 1  # AI wins
    if is_winner(board, PLAYER_O):
        return -1  # Human wins
    if is_draw(board):
        return 0  # Draw
    
    # Maximize for AI, minimize for human
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X  # AI's move
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY  # Undo the move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta pruning
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O  # Human's move
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY  # Undo the move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha pruning
        return min_eval

# Function to find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X  # AI's move
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY  # Undo the move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to play the Tic-Tac-Toe game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = PLAYER_O  # Human goes first

    while True:
        print_board(board)

        if current_player == PLAYER_X:  # AI's turn
            print("AI's move (X):")
            move = best_move(board)
            board[move[0]][move[1]] = PLAYER_X
        else:  # Human's turn
            print("Your move (O):")
            valid_move = False
            while not valid_move:
                try:
                    row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_O
                        valid_move = True
                    else:
                        print("Cell is already occupied. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter row and column as two integers between 0 and 2.")

        # Check for winner or draw
        if is_winner(board, PLAYER_X):
            print_board(board)
            print("AI wins!")
            break
        if is_winner(board, PLAYER_O):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

# Start the game
if __name__ == "__main__":
    play_game()
