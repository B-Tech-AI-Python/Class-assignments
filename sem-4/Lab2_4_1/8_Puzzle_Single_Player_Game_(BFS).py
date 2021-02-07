from time import time
from queue import Queue


class Puzzle:
    """Puzzle class to store different states and actions.

    Attributes:
        goal_state (list): list of goal state.
        num_of_instances (int): keep track of number of instances.
        state (list): current state.
        parent (list): parent state.
        action: action.

    """
    # Setting the goal state of 8-puzzle
    goal_state = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 0]

    num_of_instances = 0

    def __init__(self, state, parent, action):
        """Constructor to initialize the class members"""
        self.state = state
        self.parent = parent
        self.action = action

        Puzzle.num_of_instances += 1

    def __str__(self):
        """Display a state of 8-puzzle."""
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    def goal_test(self):
        """Compare the current state with the goal state.

        Returns:
            bool: True if successful, False otherwise.

        """
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i, j):
        """Find the legal action based on the current board position.

        Returns:
            list: A list of legal actions.

        """
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:
            # if row is 0 in board then up is disable
            legal_action.remove('U')
        elif i == 2:
            legal_action.remove('D')

        if j == 0:
            legal_action.remove('L')

        elif j == 2:
            legal_action.remove('R')

        return legal_action

    def generate_child(self):
        """Generate the child of the current state of the board."""
        children = []
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)

        legal_actions = self.find_legal_actions(i, j)

        for action in legal_actions:
            new_state = self.state.copy()

            # Swap current index with its up element
            if action == 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]

            # Swap current index with its down element
            elif action == 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]

            # Swap current index with its left element
            elif action == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]

            # Swap current index with its right element
            elif action == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]

            children.append(Puzzle(new_state, self, action))

        return children

    def find_solution(self):
        """Find the solution and states to reach the solution."""
        solution = []
        solution_states = []

        solution.append(self.action)
        solution_states.append(self)

        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
            solution_states.append(path)

        # slicing the list to remove None type element
        solution = solution[:-1]
        solution_states = solution_states[:-1]

        # reversing list as solution was being stored in reverse
        solution.reverse()
        solution_states.reverse()

        return solution, solution_states


def breadth_first_search(initial_state):
    """Function to execute for breadth first search.

    Args:
        initial_state (list): initial state of node.

    """

    start_node = Puzzle(initial_state, None, None)

    print("Initial state:")
    print(start_node)

    if start_node.goal_test():
        return start_node.find_solution()

    q = Queue()
    q.put(start_node)

    explored = []

    # Iterate the queue until empty
    while not(q.empty()):
        node = q.get()

        explored.append(node.state)

        children = node.generate_child()

        for child in children:
            if child.state not in explored:

                if child.goal_test():
                    return child.find_solution()
                q.put(child)

    return


# We have considered 3 initial state intitalized using state variable.
state = [[1, 2, 3,
          0, 4, 6,
          7, 5, 8],

         [0, 1, 3,
          4, 2, 5,
          7, 8, 6],

         [1, 2, 3,
          4, 5, 6,
          7, 8, 0]]

for i in range(0, 3):
    Puzzle.num_of_instances = 0

    t0 = time()

    bfs = breadth_first_search(state[i])

    t1 = time()-t0

    print('\nBFS:', bfs[0])

    print("Solution states:")
    for i in range(len(bfs[1])):
        print("state", i+1)
        print(bfs[1][i])
        print()
    print()

    print('Space:', Puzzle.num_of_instances)
    print('Time:', t1)

    print('------------------------------------------')

print('The end.')
