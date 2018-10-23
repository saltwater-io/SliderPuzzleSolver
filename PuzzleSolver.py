from _collections import deque
import time
import random
from anytree import NodeMixin


class Node(NodeMixin):

    def __init__(self, state, state_array, position, depth, path, heuristic=None):
        self.state = state
        self.state_array = state_array
        self.position = position
        self.depth = depth  # increment per slide
        self.heuristic = heuristic
        self.path = path  # each tile that moves in solution

    pass


SOLVED_PUZZLE = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

def check_piece(piece, puz):
    valid_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    if len(piece) > 1:
        return False

    elif piece in puz:
        return False

    elif piece in valid_nums:
        return True

    elif piece in valid_nums and piece not in puz:
        return True
    pass


def find_starting_state(puzzle):
    for i in range(3):  # i = column #, j = row
        for j in range(3):
            if puzzle[i][j] == 0:
                entry = str(i) + str(j)  # beginning state of puzzle
    return entry


def get_user_input():
    print("Hello, this program solves a 3x3 slider puzzle!")
    print("To generate a random, solvable puzzle please enter 'n'!  ")
    user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
    user_input = user_input.upper()
    while user_input != "Y" and user_input != "N":
        print("Sorry, only 'Y'/'N' or 'y'/'n' are acceptable answers. Please try again! ")
        user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
        user_input = user_input.upper()
    puzzle = []
    while user_input == 'Y':
        while len(puzzle) < 9:
            puzzle_piece = input("Please enter one number(0-8) in the order you would like it to appear:  ")
            puzzle_piece = str(puzzle_piece)
            if not check_piece(puzzle_piece, puzzle):
                print("Please enter a valid non-repeating number! ")
                if len(puzzle):
                    print("The current pieces are as follows:" + print_puzzle(puzzle))
            else:
                puzzle.append(puzzle_piece)
        if len(puzzle) == 9:
            if is_solvable(puzzle):
                print("The puzzle you entered is solvable, and will time to solution will be calculated. ")
                user_input = 'N'
            else:
                print("The puzzle you entered: " + print_puzzle(puzzle) + " is not solvable, please try again: ")
                new_input = input("If you would like a random maze generated for you enter 'N', or press any key:  ")
                puzzle.clear()
                if new_input.upper() == 'N':
                    user_input = new_input
    if user_input == 'N':
        print("A valid puzzle will now be generated for you: ")
        puzzle = generate_puzzle()
        while not is_solvable(puzzle):
            puzzle = generate_puzzle()
        print("Solvable puzzle has been generated! ")
        print("Order of pieces: " + print_puzzle(puzzle))
    if not is_solvable(puzzle):
        print("Sorry the puzzle you entered is ass like this code: ")



def solve_stack():
    visited_states = []
    pass


def solve_queue():
    visited_states = []
    pass


def solve_manhattan():
    visited_states = []
    pass


def print_puzzle(puz):
    output = ""
    for p in puz:
        output = output + " " + p
    return output


def solve_position():
    visited_states = []

def to_2d_array(puz):
    puzzle = ['0'] * 3
    count = 0
    for p in puzzle:
        puzzle[p] = ['0'] * 3
    for i in range(3):
        for j in range(3):
            puzzle[i][j] = puz[count]
            count += 1


def generate_puzzle():
    puzzle = []
    while len(puzzle) < 9:
        num = random.randint(0, 8)
        if str(num) not in puzzle:
            puzzle.append(str(num))
    return puzzle


def to_integer_array(puz):
    for i in puz:
        puz[i] = int(puz[i])
    return puz

# This function was adapted from:
# https://gist.github.com/caseyscarborough/6544636
def is_solvable(puzzle):
    # puzzle = to_2d_array(puzzle)
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(1, len(puzzle)):
            if(puzzle[i] > puzzle[j]):
                inversions += 1
        if puzzle[i] == 0 and i % 2 == 1:
            inversions += 1
    return inversions % 2 == 0


def main():
    get_user_input()


if __name__ == "__main__":
    main()
    start_state = ''
    pass

    solve_stack()
    solve_queue()
    solve_manhattan()
    solve_position()
    pass

