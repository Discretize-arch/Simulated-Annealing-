import random

# Solve the 8 puzzle using simulated annealing

# board and the goal state
board = [[2, 8, 3],
         [1, 6, 4],
         [7, 0, 5]]

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]

# directions
Directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


# create a function that returns a list of possible moves
# later our program will randomly choose one of these moves
def possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                blank_row = i
                blank_col = j
                break
    if blank_row != 0:
        moves.append('up')
    if blank_row != 2:
        moves.append('down')
    if blank_col != 0:
        moves.append('left')
    if blank_col != 2:
        moves.append('right')

    # return printed list of possible moves and moves value
    print('Possible moves:', moves)
    return moves


# 3 by 3 printout of the board
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()


# choose a random move from the list of possible moves
def random_move(move):
    r_move = move[random.randint(0, len(move) - 1)]
    # print chosen move
    print('Chosen move:', r_move)
    return r_move


# make a function that moves the blank space in the board
def move_blank(board, move):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                blank_row = i
                blank_col = j
                break
    # move the blank space
    if move == 'up':
        board[blank_row][blank_col] = board[blank_row - 1][blank_col]
        board[blank_row - 1][blank_col] = 0
    elif move == 'down':
        board[blank_row][blank_col] = board[blank_row + 1][blank_col]
        board[blank_row + 1][blank_col] = 0
    elif move == 'left':
        board[blank_row][blank_col] = board[blank_row][blank_col - 1]
        board[blank_row][blank_col - 1] = 0
    elif move == 'right':
        board[blank_row][blank_col] = board[blank_row][blank_col + 1]
        board[blank_row][blank_col + 1] = 0
    print('Board after move:')
    print_board(board)
    return board


# undo a move
def undo_move(board, move):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                blank_row = i
                blank_col = j
                break
    if move == 'up':
        board[blank_row][blank_col] = board[blank_row + 1][blank_col]
        board[blank_row + 1][blank_col] = 0
    elif move == 'down':
        board[blank_row][blank_col] = board[blank_row - 1][blank_col]
        board[blank_row - 1][blank_col] = 0
    elif move == 'left':
        board[blank_row][blank_col] = board[blank_row][blank_col + 1]
        board[blank_row][blank_col + 1] = 0
    elif move == 'right':
        board[blank_row][blank_col] = board[blank_row][blank_col - 1]
        board[blank_row][blank_col - 1] = 0
    return board


# create a function that calculates the hamming distance
# have a variable that tracks energy
# closer hamming distance will decrease energy
def hamming_distance(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal[i][j]:
                distance += 1
    return distance


# check if puzzle is solved
def is_solved(board, goal):
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal[i][j]:
                return False
    return True


# simmulated annealing algorithm. We want to go from high energy to low energy
def annealing(board, goal):
    iterations = 0
    start = board
    final_temp = 0
    # energy. We want to start with a high energy and decrease it. However, it can also rise due to randomness
    energy = 500
    temperature = energy
    old_distance = 50
    # create a while loop that runs until the board is solved
    while not is_solved(board, goal) and temperature != 0:
        moves = possible_moves(board)
        move = random_move(moves)
        board = move_blank(board, move)
        distance = hamming_distance(board, goal)
        # check if solved
        if is_solved(board, goal):
            print('Puzzle solved!')
            temperature = 0
            print("Temperature: ", temperature)
            break
        # if not solved, we need to see if the new distance is less than the old distance
        if distance < old_distance:
            # if so, we need to update the old distance
            old_distance = distance
            temperature = energy - (distance * 5)
        else:
            # if not, we need to calculate the probability of accepting the worse solution
            probability = random.random()
            # if the probability is less than 0.5, we need to accept the worse solution.
            # even though this is counterintuitive, annealing helps it from being stuck in a local minimum
            if probability < 0.5:
                old_distance = distance
                temperature = energy + (distance * 5)
            # if the probability is greater than 0.5, we need to undo the move
            else:
                board = undo_move(board, move)
                temperature = energy - (distance * 5)
        iterations += 1
        print('Iteration:', iterations)
        print('Temperature:', temperature)
        print()
    return board


# testing the main
if __name__ == '__main__':
    print(possible_moves(board))
    annealing(board, goal)
    print("Course: CS 3642"
          "\n Student name: Leiko Niwano"
          "\n Student ID: -----------"
          "\n Assignment #: 2"
          "\n Due Date: 3/27/2022"
          "\n Signature: __Leiko Niwano__")