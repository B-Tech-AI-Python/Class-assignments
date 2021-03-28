# Import the necessary libraries
from time import time
from queue import PriorityQueue
import math


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
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    heuristic = None
    evaluation_function = None
    needs_hueristic = False
    num_of_instances = 0

    def __init__(self, state, parent, action, path_cost, needs_hueristic=False):
        """Constructor of Puzzle class."""
        self.parent = parent
        self.state = state
        self.action = action

        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost

        if needs_hueristic:
            self.needs_hueristic = True
            self.generate_heuristic()
            # f = g + h
            self.evaluation_function = self.path_cost + self.heuristic

        Puzzle.num_of_instances += 1

    def __str__(self):
        """Method used to display a state of 8-puzzle.

        Returns:
            string form of current probelm state.
        """
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    def generate_heuristic(self):
        """Method used to generate a heuristic value."""
        self.heuristic = 0
        for num in range(1, 9):
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / 3)
            j = int(distance % 3)
            self.heuristic = self.heuristic + i + j

    def goal_test(self):
        """Method to compare the current state with the goal state.

        Returns:
            bool: true if states are equal, otherwise false.
        """
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i, j):
        """Find the legal actions as Up, Down, Left, Right based on each cell of state.

        Args:
            i: row position.
            j: column position.

        Returns:
            list of legal actions out of ['U', 'D', 'L', 'R'].
        """
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

        i = int(x / 3)
        j = int(x % 3)

        legal_actions = self.find_legal_actions(i, j)

        for action in legal_actions:
            new_state = self.state.copy()
            # legal action is UP
            if action == 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]

            # legal action is DOWN
            elif action == 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]

            # legal action is LEFT
            elif action == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]

            # legal action is RIGHT
            elif action == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]

            children.append(
                Puzzle(new_state, self, action, 1, self.needs_hueristic))

        return children

    def find_solution(self):
        """Method to find the solution."""
        solution = []
        solution_states = []

        solution.append(self.action)
        solution_states.append(self.state)

        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
            solution_states.append(path.state)

        solution = solution[:-1]
        solution_states = solution_states[:-1]

        solution.reverse()
        solution_states.reverse()

        return solution, solution_states


def Astar_search(initial_state):
    """Method for A-star search."""
    count = 0

    explored = []

    start_node = Puzzle(initial_state, None, None, 0, True)
    q = PriorityQueue()

    q.put((start_node.evaluation_function, count, start_node))

    while not q.empty():
        node = q.get()

        node = node[2]

        explored.append(node.state)
        if node.goal_test():
            return node.find_solution()

        children = node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                q.put((child.evaluation_function, count, child))
    return


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

    print('A*:', astar[0])

    print('\nA* solution states')
    for sol_state in astar[1]:
        for x in (3, 6, 9):
            print(sol_state[x-3:x])
        print()

    print('Space:', Puzzle.num_of_instances)
    print('\nTime:', t1)
    print()
    print('------------------------------------------')
