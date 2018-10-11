from _collections import deque


class Node():

    def __init__(self, state, state_array, position, depth, heuristic, path):
        self.state = state
        self.state_array = state_array
        self.position = position
        self.depth = depth #increment per slide
        self.heuristic = heuristic
        self.path = path #each tile that moves in solution
    pass


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



if __name__=="__main__":

    start_state = ''
    maze = ['0'] * 3
    for i in range(3):
        maze[i] = '0' * 3
        for j in range(3):
            maze[i][j] = nextLine.split('/n')

    pass


    solve_stack()
    solve_queue()
    solve_manhattan()
    solve_position()

    main()
    #put whole maze into state
    pass
