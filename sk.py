import numpy as np
from sklearn.linear_model import LogisticRegression

# Define the game environment
board = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

# Define the labels for the game states
labels = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Flatten the game states for training
X = board.reshape(9, -1)

# Train the machine learning model
model = LogisticRegression()
model.fit(X, labels)

# Function to get the computer's move
def get_computer_move(board):
    available_moves = np.where(board == 0)[0]
    move_scores = []

    for move in available_moves:
        new_board = np.copy(board)
        new_board[move] = 1
        move_scores.append(model.predict_proba(new_board.reshape(1, -1))[0][1])

    best_move = available_moves[np.argmax(move_scores)]
    return best_move

# Function to print the game board
def print_board(board):
    for row in board.reshape(3, -1):
        print(row)

# Main game loop
player_turn = True

while True:
    print_board(board)

    if player_turn:
        # Player's turn
        move = int(input("Enter your move (0-8): "))
        if board[move] != 0:
            print("Invalid move! Try again.")
            continue
        board[move] = -1
    else:
        # Computer's turn
        move = get_computer_move(board)
        board[move] = 1
        print("Computer's move:", move)

    # Check for game over condition
    if np.abs(np.sum(board)) == 3 or len(np.where(board == 0)[0]) == 0:
        print_board(board)
        print("Game over!")
        break

    player_turn = not player_turn
