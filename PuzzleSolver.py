ffrom _collections import deque
import time
import random
from anytree import NodeMixin


class Node(NodeMixin):

    def __init__(self, state, state_array, position, depth, heuristic, path):
        self.state = state
        self.state_array = state_array
        self.position = position
        self.depth = depth  # increment per slide
        self.heuristic = heuristic
        self.path = path  # each tile that moves in solution

    pass

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
                entry = str(i) + str(j)  # begining state of puzzle
    return entry


def check_puzzle_validity(puzzle):
    return False
    pass


def get_user_input():
    print("Hello, this program solves a 3x3 slider puzzle!")
    user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
    user_input = user_input.upper()
    while user_input != "Y" and user_input != "N":
        print("Sorry, only Y/N or y/n are acceptable answers. Please try again!")
        user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
        user_input = user_input.upper()
    puzzle = []
    if user_input == 'Y':
        while len(puzzle) < 9:
            puzzle_piece = input("Please enter one number(0-8) in the order you would like it to appear:  ")
            puzzle_piece = str(puzzle_piece)
            if not check_piece(puzzle_piece, puzzle):
                print("Please enter a valid non-repeating number! ")
                if len(puzzle):
                    output = ""
                    for p in puzzle:
                        output = output + " " + p
                    print("The current pieces are as follows:" + output)
            else:
                puzzle.append(puzzle_piece)
    else:
        print("A valid puzzle will now be generated for you: ")
    if not check_puzzle_validity(puzzle):
        print("Sorry the puzzle you entered is ass like this code")



def solve_stack():
    visited_states = []
    pass


def solve_queue():
    visited_states = []
    pass


def solve_manhattan():
    visited_states = []
    pass


def solve_position():
    visited_states = []


def main():
    pass


def is_solvable(puzzle):
    pass
    # for i in puzzle:


def main():
    get_user_input()


if __name__ == "__main__":
    main()
    start_state = ''
    maze = ['0'] * 3
    for i in range(3):
        maze[i] = '0' * 3
        for j in range(3):
            pass
            # maze[i][j] =

    pass

    solve_stack()
    solve_queue()
    solve_manhattan()
    solve_position()
    pass
