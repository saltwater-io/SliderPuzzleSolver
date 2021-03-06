from _collections import deque
import random
from timeit import default_timer as timer
import copy
import heapq as heap


# Class for structure node builder for each state of puzzle
# Holds state, the state in maze I.E 60 would be the entry 'E' for the maze
class Node:
    state_array = []
    position = ''
    depth = 0
    current_path = []

    def __init__(self, state_array, position, depth, current_path=None, heuristic=None):
        self.state_array = state_array
        self.position = position
        self.depth = depth  # increment per slide
        self.heuristic = heuristic  # A* heuristic
        self.current_path = current_path


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


# Goals State is used to validate the completeness of the puzzle
GOAL_STATE = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
default_puzzle = [['7', '8', '3'], ['4', '1', '5'], ['6', '0', '2']]
default_puzzle1 = [['2', '0', '3'], ['1', '8', '5'], ['4', '7', '6']]
heuristic_position = {'00': '1', '01': '2', '02': '3', '10': '4', '11': '5', '12': '6', '20': '7', '21': '8', '22': '0'}


# Checks user entry to see if it is a valid option
def check_piece(piece, puz):
    valid_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    if len(piece) > 1:
        return False

    elif piece in puz:
        return False

    elif piece in valid_nums and piece not in puz:
        return True
    pass


# Finds position of 0 in the slider puzzle for further examination
def find_open_position(puzzle):
    for i in range(3):  # i = column #, j = row
        for j in range(3):
            if puzzle[i][j] == '0':
                entry = str(i) + str(j)  # Open spot in puzzle
    return entry


# Begins program by display options and receiving user input
def begin():
    print(" ")
    print("Hello, this program solves a 3x3 slider puzzle!")
    print(" ")
    print("To generate a random, puzzle please enter 'n'!  ")

    user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
    user_input = user_input.upper()

    # Forces user to choose a valid option
    while user_input != "Y" and user_input != "N":
        print("Sorry, only 'Y'/'N' or 'y'/'n' are acceptable answers. Please try again! ")
        user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
        user_input = user_input.upper()
    puzzle = []

    # If user chooses 'Y', user proceeds to input puzzle
    if user_input == 'Y':

        # while the puzzle is less than 3 x 3 and the input is not exit or N
        while len(puzzle) < 9 and user_input != 'XIT' and user_input != 'N':

            puzzle_piece = input("Please enter one number(0-8) in the order you would like it to appear:  ")
            puzzle_piece = str(puzzle_piece)  # Converts user input -> Precautionary cast

            # Checks to see if user input is valid
            if not check_piece(puzzle_piece, puzzle):
                print("Please enter a valid non-repeating number! ")

                if len(puzzle):  # Displays current puzzle to user for ease of access
                    print("The current pieces are as follows:" + print_puzzle(puzzle))
            else:
                puzzle.append(puzzle_piece)  # Adds piece to puzzle

        #  Puzzle is correct length, notify user and proceed.
        if len(puzzle) == 9:
            print("The puzzle you entered will now try to be solved:  " + print_puzzle(puzzle))
            user_input = 'XIT'

    # User wants to generate a random puzzle to be solved
    if user_input == 'N':
        print("A puzzle will now be generated for you. ")
        print("")
        # Generates puzzle
        puzzle = generate_puzzle()
        # while not is_solvable(puzzle):
        #     puzzle = generate_puzzle()
        print("Puzzle has been generated! ")
        print("Order of pieces: " + print_puzzle(puzzle))

    # Menu for the user to choose which way the puzzle is solved
    print("There are four available options to solve the puzzle: ")

    print("")
    menu = {'1': "Breath First Search.",
            '2': "Depth First Search.",
            '3': "Tile Position Heuristic.",
            '4': "Manhattan Distance Heuristic.",
            '5': "Enter a new puzzle.",
            '6': "Quit."}

    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = str(input("Please make a selection:"))
        print(" ")
        if selection == '1':
            solve_queue(puzzle)
        elif selection == '2':
            solve_stack(puzzle)
        elif selection == '3':
            solve_position(puzzle)
        elif selection == '4':
            solve_manhattan(puzzle)
        elif selection == '5':
            user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
            user_input = user_input.upper()
            # Forces user to choose a valid option
            while user_input != "Y" and user_input != "N":
                print("Sorry, only 'Y'/'N' or 'y'/'n' are acceptable answers. Please try again! ")
                user_input = input("Would you like to input your own maze using non repeating numbers 0-8?: y/n  ")
                user_input = user_input.upper()
            puzzle = []
            while True:
                while len(puzzle) < 9 and user_input != 'N':

                    puzzle_piece = input("Please enter one number(0-8) in the order you would like it to appear:  ")
                    puzzle_piece = str(puzzle_piece)

                    # Checks to see if user input is valid
                    if not check_piece(puzzle_piece, puzzle):
                        print("Please enter a valid non-repeating number! ")

                        if len(puzzle):  # Displays current puzzle to user for ease of access
                            print("The current pieces are as follows:" + print_puzzle(puzzle))
                    else:
                        puzzle.append(puzzle_piece)  # Adds piece to puzzle

                #  Puzzle is correct length, notify user and proceed.
                if len(puzzle) == 9:
                    print("The puzzle you entered will now try to be solved:  " + print_puzzle(puzzle))
                    print(" ")
                    break
                if user_input == 'N':
                    print("A puzzle will now be generated for you. ")
                    print("")

                    # Generates puzzle
                    puzzle = generate_puzzle()
                    print("Puzzle has been generated! ")
                    print("Order of pieces: " + print_puzzle(puzzle))
                    print(" ")
                    break
        elif selection == '6':
            break
        else:
            print("Please choose 1, 2, 3, 4, or 5 to quit! ")


# Solves puzzle via Breadth-First Search (queue)
def solve_queue(puzzle):
    queue = deque([])  # Queue
    visited_states = {}  # Visited_States

    depth = 0

    puzzle = to_2d_array(puzzle)  # Transforms puzzle to 2-d array
    start = timer()  # timer start

    path = [to_string(puzzle)]  # Path of moves preformed

    # Change 'puzzle' to 'default_puzzle' for a solvable example
    node = Node(puzzle, find_open_position(puzzle), depth, path)  # Origin state
    visited_states[to_string(node.state_array)] = 1  # adds visited states as an in-order string

    solved = True  # Sets puzzle to solved as default state
    queue.append(node)  # Adds origin state to queue
    node = queue.popleft()  # Pops origin as node

    #  Loop walks through puzzle and checks if goal state is reached
    while node.state_array != GOAL_STATE:
        children = get_children(node)  # Child States

        for child in children:  # Has the state been visited before?
            if to_string(child) in visited_states:
                pass
            elif to_string(child) not in visited_states:  # If the state is fresh
                visited_states[to_string(child)] = 1  # Adds new state to visited states

                new_path = copy.deepcopy(node.current_path)  # Gets path of parent and adds current state
                new_path.append(to_string(child))

                new_node = Node(child, find_open_position(child), node.depth + 1, current_path=new_path)  # New node
                queue.append(new_node)  # Adds node to queue

        if len(queue):  # if Queue not empty
            node = queue.popleft()
        else:
            print("Sorry, puzzle not solvable!")
            solved = False
            break

    end = timer()
    time = end - start

    if solved:
        print("Path: ")
        path = ''
        for state in node.current_path:
            path = path+" "+state
        print(path)
        print("------------")
        print("Breadth First Search solution found in: " + str(time) + " seconds at " + str(node.depth) + " depth.")
        print('Nodes explored: ' + str(len(visited_states)))
        print("  ")

    else:
        print("BFS took: " + str(time) + " seconds, and explored " + str(len(visited_states)) + " nodes.")
        print(" ")


# Solves the 3x3 slider puzzle using depth first search (stack).
def solve_stack(puzzle):
    stack = Stack()  # Queue
    visited_states = {}  # Visited_States

    depth = 0
    puzzle = to_2d_array(puzzle)  # Transforms puzzle into 2-d array
    start = timer()  # timer start

    path = [to_string(puzzle)]
    node = Node(puzzle, find_open_position(puzzle), depth, path)  # Origin state

    visited_states[to_string(node.state_array)] = 1  # adds visited states as a key in dictionary O(1)

    stack.push(node)  # Adds origin state to stack
    node = stack.pop()  # Pops origin as node
    solved = True

    #  Loop walks through puzzle and checks if goal state is reached
    while node.state_array != GOAL_STATE:
        children = get_children(node)  # Child States
        for child in children:
            if to_string(child) in visited_states:
                pass
            elif to_string(child) not in visited_states:
                visited_states[to_string(child)] = 1  # Adds new state to visited states
                # Creates new node state
                new_node = Node(child, find_open_position(child), node.depth + 1)
                stack.push(new_node)  # Pushes state onto stack

        if stack.isEmpty():  # Checks if puzzle is solved
            if node.state_array == GOAL_STATE:
                solved = True
                pass
            else:
                print(" ")
                print("Sorry, puzzle not solvable!")
                print(" ")
                solved = False
                break
        else:
            node = stack.pop()
    end = timer()
    time = end - start
    if solved:  # If puzzle if solved:
        print("------------")
        print("Depth First Search solution found in: " + str(time) + " seconds at depth: " + str(node.depth))
        print('Nodes explored: ' + str(len(visited_states)))
        print(" ")
    else:
        print("DFS took: " + str(time) + " seconds, and explored " + str(len(visited_states)) + " nodes.")
        print(" ")


# Solves a puzzle using the Manhattan distance heuristic
# which is total number of moves of each piece from the goal state
def solve_manhattan(puzzle):
    queue = []  # Queue

    visited_states = {}  # Visited_States

    depth = 0
    puzzle = to_2d_array(puzzle)  # Transforms puzzle to 2-d array
    start = timer()  # timer start

    path = [to_string(puzzle)]  # Adds starting state to path
    # Creates origin node
    node = Node(puzzle, find_open_position(puzzle), depth, path, get_manhattan(puzzle))  # Origin state
    visited_states[to_string(node.state_array)] = 1  # adds visited states as an in-order string

    heap.heappush(queue, (node.heuristic, 0, node))  # Adds origin state to queue making it a heap
    temp_tuple = heap.heappop(queue)  # Gets tuple

    node = temp_tuple[2]  # Grabs node from tuple
    solved = True

    #  Loop walks through puzzle and checks if goal state is reached
    while node.state_array != GOAL_STATE:
        children = get_children(node)  # Child States
        for child in children:  # Check for previously visited states
            if to_string(child) in visited_states:
                pass
            elif to_string(child) not in visited_states:

                visited_states[to_string(child)] = 1  # Adds new state to visited states

                new_path = copy.deepcopy(node.current_path)  # Creates a new path and adds itself to the path
                new_path.append(to_string(child))  # Creates a new node
                new_node = Node(child, find_open_position(child), node.depth + 1, current_path=new_path,
                                heuristic=get_manhattan(child) + node.depth + 1)
                heap.heappush(queue, (new_node.heuristic, len(visited_states), new_node))  # Pushes onto heap

        if queue:  # Queue is not empty
            node = heap.heappop(queue)
            node = node[2]

        else:  # Queue is empty and goal state not achieved
            print(" ")
            print("Sorry, puzzle not solvable!")
            print(" ")
            solved = False
            break

    end = timer()
    time = end - start
    if solved:
        print("Path: ")
        path = ""
        for state in node.current_path:
            path = path+" "+state
        print(path)

        print("----------------")
        print("A* Misplaced tile solution found in: " + str(time) + " seconds at " + str(node.depth) + " depth")
        print('Nodes explored: ' + str(len(visited_states)))
        print("  ")

    else:
        print("A* # Moves Search took: " + str(time) + " seconds, and explored " + str(len(visited_states)) + " nodes.")
        print(" ")
    # print(len(visited_states))


# Solves 3x3 slider puzzle using A* misplaced tile heuristic
def solve_position(puzzle):
    queue = []  # Queue
    visited_states = {}  # Visited_States

    depth = 0
    puzzle = to_2d_array(puzzle)  # Transforms puzzle to 2-d array
    start = timer()  # timer start

    path = [to_string(puzzle)]  # Walked path

    node = Node(puzzle, find_open_position(puzzle), depth, path, get_position(puzzle))  # Origin state

    visited_states[to_string(node.state_array)] = 1  # adds visited states as an in-order string

    heap.heappush(queue, (node.heuristic, 0, node))  # Adds origin state to queue

    temp_tuple = heap.heappop(queue)
    node = temp_tuple[2]  # Pops origin as node

    solved = True
    #  Loop walks through puzzle and checks if goal state is reached
    while node.state_array != GOAL_STATE:
        children = get_children(node)  # Child States
        for child in children:
            if to_string(child) in visited_states:
                pass
            elif to_string(child) not in visited_states:
                visited_states[to_string(child)] = 1  # Adds new state to visited states

                new_path = copy.deepcopy(node.current_path)
                new_path.append(to_string(child))  # Creates new path from parent and adds itself to it.

                new_node = Node(child, find_open_position(child), node.depth + 1, current_path=new_path,
                                heuristic=get_position(child) + node.depth + 1)
                heap.heappush(queue, (new_node.heuristic, len(visited_states), new_node))  # Adds to heap

        if queue:  # if Queue isn't empty
            node = heap.heappop(queue)
            node = node[2]
        else:  # Queue is empty and goal state has not been reached
            print(" ")
            print("Sorry, puzzle not solvable!")
            print(" ")
            solved = False
            break
    end = timer()
    if solved:  # If puzzle has been solved, print path to solution
        path = ''
        for state in node.current_path:
            path = path+" "+state
        print(path)
        time = end - start
        print("-------------------")
        print("A* Misplaced Tile solution found in: " + str(time) + " seconds at " + str(node.depth) + " depth.")
        print('Nodes explored: ' + str(len(visited_states)))
        print("  ")
    else:
        time = end - start
        print("A* Misplaced tile search took: " + str(time) + " seconds, and explored " + str(len(visited_states)) + " nodes.")
        print(" ")
    # print(len(visited_states))


# Function returns the current manhattan distance
# By checking # steps each piece is away from its final destination
# Adapted from: https://stackoverflow.com/questions/12526792/manhattan-distance-in-a
def get_manhattan(state):
    manhattan = 0  # Total # of misplaced tiles by Steps
    for x in range(3):
        for y in range(3):
            current = int(state[x][y])  # Value of tile
            if current != 0:
                xtarget = (current - 1) // 3  # Gets target location of
                ytarget = (current - 1) % 3
                dx = x - xtarget
                dy = y - ytarget
                manhattan += abs(dx) + abs(dy)
    return manhattan


# Returns position heuristic for puzzle pieces not in
# Goal State location
def get_position(state):
    position = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != heuristic_position[str(i) + str(j)]:
                position += 1
    return position


# Prints puzzle for output format
def print_puzzle(puz):
    output = ""
    for p in puz:
        output = output + " " + p
    return output


# Gets child node positions of the current state
# Takes the current state as parameter
# Returns a list of future states aka children from current state
def get_children(node):
    state = node.state_array
    children = []  # List of possible moves after
    possible_moves = []  # Temp List of possible moves
    r = int(node.position[0])  # Row
    c = int(node.position[1])  # Column

    if r == 0 and c == 0:
        possible_moves.append('01')
        possible_moves.append('10')
    elif r == 0 and c == 1:  # Puzzle slots: RC
        possible_moves.append('00')  # 00 01 02
        possible_moves.append('02')  # 10 11 12
        possible_moves.append('11')  # 20 21 22

    elif r == 0 and c == 2:
        possible_moves.append('01')
        possible_moves.append('12')

    elif r == 1 and c == 0:  # Puzzle slots: RC
        possible_moves.append('00')  # 00 01 02
        possible_moves.append('11')  # 10 11 12
        possible_moves.append('20')  # 20 21 22

    elif r == 1 and c == 1:
        possible_moves.append('01')
        possible_moves.append('10')
        possible_moves.append('12')
        possible_moves.append('21')

    elif r == 1 and c == 2:  # Puzzle slots: RC
        possible_moves.append('02')  # 00 01 02
        possible_moves.append('22')  # 10 11 12
        possible_moves.append('11')  # 20 21 22

    elif r == 2 and c == 0:
        possible_moves.append('10')
        possible_moves.append('21')

    elif r == 2 and c == 1:  # Puzzle slots: RC
        possible_moves.append('20')  # 00 01 02
        possible_moves.append('11')  # 10 11 12
        possible_moves.append('22')  # 20 21 22

    elif r == 2 and c == 2:
        possible_moves.append('21')
        possible_moves.append('12')

    for move in possible_moves:
        children.append(slide_tiles(state, node.position, move))
    return children


# Converts puzzle from string to 2D array
def to_2d_array(puz):
    puzzle = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    count = 0
    for i in range(3):
        for j in range(3):
            puzzle[i][j] = puz[count]
            count += 1
    return puzzle


# Received state and generates a new state by
# Sliding the tiles from move into open space 'Current'
def slide_tiles(state, current, move):
    temp_state = copy.deepcopy(state)

    # Swaps the tiles in a very smooth way
    temp_state[int(current[0])][int(current[1])], temp_state[int(move[0])][int(move[1])] = \
        temp_state[int(move[0])][int(move[1])], temp_state[int(current[0])][int(current[1])]
    return temp_state


# Converts 2-d array into string
def to_string(puz):
    state = ''
    for i in range(3):
        for j in range(3):
            state = state + puz[i][j]
    return state

# Generates a puzzle
def generate_puzzle():
    puzzle = []
    while len(puzzle) < 9:
        num = random.randint(0, 8)
        if str(num) not in puzzle:
            puzzle.append(str(num))
    return puzzle


# This function was adapted from:
# https://gist.github.com/caseyscarborough/6544636
# Used for testing purposes
def is_solvable(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inversions += 1
        if puzzle[i] == 0 and i % 2 == 1:
            inversions += 1
    return inversions % 2 == 0


if __name__ == "__main__":
    begin()
    pass
