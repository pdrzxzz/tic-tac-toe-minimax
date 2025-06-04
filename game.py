
"""
Author: Emanuel Pedroza
Date: 04/06/2025
Description: Implementation of a Tic-Tac-Toe game where a human plays against an AI.
             The AI uses the Minimax algorithm with Alpha-Beta pruning to make optimal moves.
"""

import math

#####
# Minimax algorithm with alpha-beta pruning.
# This function evaluates possible moves recursively to choose the best one for the AI.
# The recursion is started by best_move function
# Parameters:
# - board: current game board (3x3 list)
# - AISymbol: symbol used by the AI
# - playerSymbol: symbol used by the human player
# - alpha, beta: values used in alpha-beta pruning
# - depth: current depth of the recursion
# - maximizing: boolean indicating if it's the AI's turn (True) or the player's (False)
#
# Returns:
# - An integer score representing the evaluation of the board
#####

def minimax(board, AISymbol, playerSymbol, alpha=-math.inf, beta=math.inf, depth=0, maximizing=False):
    # Checks winner, important since the algorithm is recursive
    result = isGameOver(board)
    if result == AISymbol:
        return 10 - depth # How faster wins better
    elif result == playerSymbol:
        return -1
    elif result == 'Draw':
        return 0

    if maximizing:
        # Starts with the worst possible value for alpha (wants to maximize this)
        max_value = -math.inf
        # Goes through all possible moves
        for (i, j) in possible_moves(board):
            # Simulates the move
            board[i][j] = AISymbol
            # Recursively calls minimax for the opponent (maximizing = False)
            value = minimax(board, AISymbol, playerSymbol, alpha, beta, depth+1)
            # Undoes the simulation (backtracking)
            board[i][j] = ' '
            max_value = max(max_value, value)
            alpha = max(alpha, value)
            # This branch can be ignored
            if beta <= alpha:
                break
        return max_value
    else:
        # Starts with the worst possible value for beta (wants to minimize this)
        min_value = math.inf
        for (i, j) in possible_moves(board):
            # Simulates the move
            board[i][j] = playerSymbol
            # Recursively calls minimax for the opponent (maximizing = True)
            value = minimax(board, AISymbol, playerSymbol, alpha, beta, depth+1, maximizing=True)
            # Undoes the simulation (backtracking)
            board[i][j] = ' '
            min_value = min(min_value, value)
            beta = min(beta, value)
            # This branch can be ignored
            if beta <= alpha:
                break
        return min_value

#####
# Determines the best possible move for the AI based on the current board state.
#
# Parameters:
# - board: current game board
# - AISymbol: symbol used by the AI
# - playerSymbol: symbol used by the player
#
# Returns:
# - Tuple (i, j) representing the row and column of the best move
#####
def best_move(board, AISymbol, playerSymbol):
    max_value = -math.inf
    move = None
    # The starter of the minimax algorithm
    for (i, j) in possible_moves(board):
        board[i][j] = AISymbol
        value = minimax(board, AISymbol, playerSymbol)
        board[i][j] = ' '
        if value > max_value:
            max_value = value
            move = (i, j)
    return move

#####
# Main game loop that allows the player to play against the AI.
#####
def play():
    # Init board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # The user selects its symbol
    playerSymbol = input("Do you want to be X or O? ").upper()
    while playerSymbol not in ['X', 'O']:
        playerSymbol = input("Choose X or O: ").upper()
    AISymbol = 'O' if playerSymbol == 'X' else 'X'

    # X always starts
    turn = 'X'  

    while True:
        # Show current board state
        show_board(board)

        # Endgame check
        winner = isGameOver(board)
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        # Player turn
        if turn == playerSymbol:
            try:
                i, j = map(int, input("Your move (row and column, from 0 to 2): ").split())
                if board[i][j] == ' ':
                    board[i][j] = playerSymbol
                    turn = AISymbol
                else:
                    print("Position already taken. Try again.")
            except:
                print("Invalid input. Enter two numbers from 0 to 2.")
        # IA turn
        else:
            print("AI is thinking...")
            i, j = best_move(board, AISymbol, playerSymbol)
            board[i][j] = AISymbol
            turn = playerSymbol

#####
# Displays the current board in a readable format.
#
# Parameters:
# - board: current game board
#####
def show_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

#####
# Checks whether the game is over.
#
# Parameters:
# - board: current game board
#
# Returns:
# - 'X' if X wins
# - 'O' if O wins
# - 'Draw' if the board is full with no winner
# - None if the game is still ongoing
#####

def isGameOver(board):
    rows = board
    columns = [list(col) for col in zip(*board)]
    diagonals = [[board[i][i] for i in range(3)],
                 [board[i][2 - i] for i in range(3)]]

    for line in rows + columns + diagonals:
        if line == ['X'] * 3:
            return 'X'
        elif line == ['O'] * 3:
            return 'O'

    # If all positions are not empty, the board is full (Draw).
    if all(position != ' ' for row in board for position in row):
        return 'Draw'

    return None

#####
# Returns a list of available moves on the board.
#
# Parameters:
# - board: current game board
#
# Returns:
# - List of tuples (i, j) representing empty cells
#####
def possible_moves(board):
    # Checks if the position is empty, if so, includes it in the return list.
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Start the game
if __name__ == "__main__":
    play()
