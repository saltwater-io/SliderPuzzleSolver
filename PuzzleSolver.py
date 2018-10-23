from _collections import deque
import time
import random
from anytree import NodeMixin
from timeit import default_timer as timer


# Class for structure node builder for each state of puzzle
# Holds state, the state in maze I.E 60 would be the entry 'E' for the maze
class Node(NodeMixin):

    def __init__(self, state, state_array, position, depth, path, heuristic=None):
        self.state = state
        self.state_array = state_array
        self.position = position
        self.depth = depth  # increment per slide
        self.heuristic = heuristic
        self.path = path  # each tile that moves in solution


# Generic stack: code taken from http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html
# Im using this stack as opposed to the precompiled imported one because this code is much cleaner
class Stack:
    def __init__(self):  # initial constructor
        self.items = []

    def isEmpty(self):  # is stack empty?
        return self.items == []

    def push(self, item):  # Pushes item onto stack
        self.items.append(item)

    def pop(self):  # Pops item off stack
        return self.items.pop()

    def peek(self):  # Peeks at the last value added to stack
        return self.items[len(self.items) - 1]

    def size(self):  # Returns size of stack
        return len(self.items)


GOAL_STATE = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
default_puzzle = []

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


def begin():

    print("Hello, this program solves a 3x3 slider puzzle!")
    print("To generate a random, solvable puzzle please enter 'n'!  ")

    user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
    user_input = user_input.upper()

    while user_input != "Y" and user_input != "N":
        print("Sorry, only 'Y'/'N' or 'y'/'n' are acceptable answers. Please try again! ")
        user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
        user_input = user_input.upper()
    puzzle = []

    if user_input == 'Y':

        while len(puzzle) < 9 and user_input != 'XIT' and user_input != 'N':
            puzzle_piece = input("Please enter one number(0-8) in the order you would like it to appear:  ")
            puzzle_piece = str(puzzle_piece)

            if not check_piece(puzzle_piece, puzzle):
                print("Please enter a valid non-repeating number! ")

                if len(puzzle):
                    print("The current pieces are as follows:" + print_puzzle(puzzle))
            else:
                puzzle.append(puzzle_piece)

        if len(puzzle) == 9:
            print("The puzzle you entered will now try to be solved:  " + print_puzzle(puzzle))
            # if is_solvable(puzzle):
            #     print("The puzzle you entered is solvable, and will time to solution will be calculated. ")
            user_input = 'XIT'
            # else:
            #     print("The puzzle you entered: " + print_puzzle(puzzle) + " is not solvable, please try again: ")
            #     new_input = input("If you would like a random maze generated for you, enter 'N', or press any key:  ")
            #     if new_input.upper() == 'N':
            #         user_input = new_input.upper()
            #     puzzle.clear()

    if user_input == 'N':
        print("A valid puzzle will now be generated for you. ")
        print("")
        puzzle = generate_puzzle()
        while not is_solvable(puzzle):
            puzzle = generate_puzzle()
        print("Solvable puzzle has been generated! ")
        print("Order of pieces: " + print_puzzle(puzzle))


    print("There are four available options to solve the puzzle: ")
    print("")
    print("Option 1: Breath First Search.")
    print("Option 2: Depth First Search.")
    print("Option 3: Tile Position Heuristic - In progress.")
    print("Option 4: Manhattan Distance Heuristic - In progress.")
    print("Enter 'X' to quit!")

    print("")

    choice = input("Which would you like to choose?: ")
    choice = str(choice).upper()

    while choice != 'X' and choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print()
        choice = input("Please choose 1, 2, 3, 4, or X to quit! ")

    while choice != 'X':

        if choice == '1':
            solve_queue(puzzle)

        elif choice == '2':
            solve_stack(puzzle)

        elif choice == '3':
            solve_position(puzzle)

        elif choice == '4':
            solve_manhattan(puzzle)




def solve_queue(puzzle):
    queue = deque([])
    visited_states = []
    start = timer()
    node = Node(puzzle, to_2d_array(puzzle), find_starting_state(puzzle), 0, [])
    queue.append(node)
    while queue.pop().state_array != GOAL_STATE:


    end = timer()
    time = start - end


def solve_stack(puzzle):
    stack = Stack()
    start = timer()
    visited_states = []
    end = timer()
    time = start - end
    pass


def solve_manhattan(puzzle):
    start = timer()
    visited_states = []
    end = timer()
    time = start - end

def solve_position(puzzle):
    start = timer()
    visited_states = []
    end = timer()
    time = start - end



def get_manhattan(state):
    pass


def get_postion(state):
    pass

def print_puzzle(puz):
    output = ""
    for p in puz:
        output = output + " " + p
    return output


# Gets child node positions of the current state
# Takes the maze and current state as parameters
# Returns a list of positions of valid children from current state
def get_children(node):
    state = node.state_array
    children = []  # List of children
    temp_state = ''
    r = int(node.position[0])  # Row
    c = int(node.position[1])  # Column

    if (r == 0) and c == 0:
        children.append()

    # If column is not farthest left column, check value of position directly left of current state
    if (c != 0) and maze[r][c - 1] == 'P' or maze[r][c - 1] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r) + str(c - 1))

    # If not bottom row, check value of position directly to the bottom of current state
    if (r != 9) and maze[r - 1][c] == 'P' or maze[r - 1][c] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r - 1) + str(c))

    # If column is not farthest right column, check value of position directly right of current state
    if (c != 9) and maze[r][c + 1] == 'P' or maze[r][c + 1] == 'X':  # If maze value is 'X', or 'P' add to children
        children.append(str(r) + str(c + 1))

    return children


def to_2d_array(puz):
    puzzle = ['0'] * 3
    count = 0
    for p in puzzle:
        puzzle[p] = ['0'] * 3
    for i in range(3):
        for j in range(3):
            puzzle[i][j] = puz[count]
            count += 1


def to_string(puz):
    state = ''
    for i in range(3):
        for j in range(3):
            state = state + puz[i][j]


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
    begin()


if __name__ == "__main__":
    main()

