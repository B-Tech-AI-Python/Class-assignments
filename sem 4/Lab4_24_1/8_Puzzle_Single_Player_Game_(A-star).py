from time import time
from queue import PriorityQueue


class Puzzle:
    """Puzzle class to store different states and actions.

    Attributes:
        goal_state (list): list of goal state.
        num_of_instances (int): keep track of number of instances.
        heuristic: heuristic value (h).
        evaluation_function: evaluated value (f).
        needs_hueristic (bool): True or False.
        state (list): current state.
        parent (list): parent state.
        action: action.
        path_cost: path cost (g).

    """
    # Setting the goal state of 8-puzzle
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    num_of_instances = 0

    heuristic = None
    evaluation_function = None
    needs_hueristic = False

    def __init__(self, state, parent, action, path_cost, needs_hueristic=False):
        self.parent = parent
        self.state = state
        self.action = action
        # calculating the path_cost as the sum of its parent cost and path_cost
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost

        if needs_hueristic:
            self.needs_hueristic = True
            self.generate_heuristic()
            # calculate the expression as f = g + h
            self.evaluation_function = self.path_cost + self.heuristic

        # incrementing the number of instance by 1
        Puzzle.num_of_instances += 1

    def __str__(self):
        """Method used to display a state of 8-puzzle."""
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    def generate_heuristic(self):
        """Method used to generate a heuristic value."""
        self.heuristic = 0
        for num in range(1, 9):
            # calculate the heuristic value as manhattan distance which is the absolute
            # difference between current state and goal state.
            # Use index() method to get the index of num in state
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / 3)
            j = int(distance % 3)
            self.heuristic = self.heuristic + i + j

    def goal_test(self):
        """Method used to compare the current state with the goal state."""
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i, j):
        """Method ro find legal actions on each cell of state."""
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == 2:  # down is disable
            legal_action.remove('D')
        if j == 0:  # left is disable
            legal_action.remove('L')
        elif j == 2:  # right is disable
            legal_action.remove('R')

        return legal_action

    def generate_child(self):
        """Method to generate the child of the current state of the board."""
        children = []
        x = self.state.index(0)
        # generate the row (i) & col (j) position based on the current index of 0 on the board
        i = int(x / 3)
        j = int(x % 3)
        # call the method to find the legal actions based on i and j values
        legal_actions = self.find_legal_actions(i, j)

        for action in legal_actions:
            new_state = self.state.copy()
            # legal action is UP
            if action == 'U':
                # Swapping between current index of 0 with its up element on the board
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]

            # legal action is DOWN
            elif action == 'D':
                # Swapping between current index of 0 with its down element on the board
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]

            # legal action is LEFT
            elif action == 'L':
                # Swapping between the current index of 0 with its left element on the board
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]

            # legal action is RIGHT
            elif action == 'R':
                # Swapping between the current index of 0 with its right element on the board
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]

            # Append the new_state of Puzzle object with parent, action,path_cost is 1, its needs_hueristic flag
            children.append(
                Puzzle(new_state, self, action, 1, self.needs_hueristic))

        # return the children
        return children

    def find_solution(self):
        """Method to find the solution."""
        solution = []
        solution_states = []

        solution.append(self.action)
        solution_states.append(self)

        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
            solution_states.append(path)

        solution = solution[:-1]
        solution_states = solution_states[:-1]

        solution.reverse()
        solution_states.reverse()

        return solution, solution_states


def Astar_search(initial_state):
    """Function for A-star search.
    
    Attributes:
        initial_state: initial state.

    """
    count = 0
    explored = []

    start_node = Puzzle(initial_state, None, None, 0, True)
    print(start_node)

    q = PriorityQueue()
    q.put((start_node.evaluation_function, count, start_node))

    while not q.empty():
        # get the current node of a queue
        node = q.get()
        # extract the current node of a PriorityQueue
        node = node[2]

        # Append the state of node in the explored list as node.state
        explored.append(node.state)
        if node.goal_test():
            return node.find_solution()

        # call the generate_child method to generate the child node of current node
        children = node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                # put a tuple with child.evaluation_function, count, child into PriorityQueue
                q.put((child.evaluation_function, count, child))
    return


# Start executing the 8-puzzle with setting up the initial state
# Here we have considered 3 initial state intitalized using state variable
state = [[1, 3, 4,
          8, 6, 2,
          7, 0, 5],

         [2, 8, 1,
          0, 4, 3,
          7, 6, 5],

         [2, 8, 1,
          4, 6, 3,
          0, 7, 5]]

for i in range(0, 3):
    Puzzle.num_of_instances = 0

    t0 = time()

    astar = Astar_search(state[i])

    t1 = time() - t0

    print("Solution states:")
    for i in range(len(astar[1])):
        print("state", i+1)
        print(astar[1][i])
        print()
    print()

    print('A*:', astar[0])

    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()
    print('------------------------------------------')
