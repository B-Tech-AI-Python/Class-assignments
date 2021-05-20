"""Program to implement BFS for water jug problem using Python.

There are 2 jugs, one of 'm' liters one of 'n' liters where (0 < m < n). The jugs are 
initially empty. The jugs don't have any measuring markings. The jugs have to be 
used to measure 'x' liters of water where (x < n). The objective of the problem 
is to find the minimum number of operations performed to get 'x' liters of water in 
one of the jugs.

Operations:
1.	Fill the first jug.
2.	Fill the second jug.
3.	Empty the first jug.
4.	Empty the second jug.
5.	Pour the first jug into the second jug.
6.	Pour the second jug into the first jug.

"""
# imports
from collections import deque


def get_index(node):
    """Returns a key value for a given node.

    Attributes:
        node (list): list of two integers representing current state of the jugs.
    """

    return pow(7, node[0]) * pow(5, node[1])



def get_vol():
    """Accept volumes of the jugs as an input from the user.

    Reuturns:
        jugs (list): list of two integeres representing volumes of the jugs.
    """

    print("Enter maximum volumes of jugs")
    jugs = []

    temp = int(input("Enter volume of first jug (> 1): "))
    while temp < 1:
        temp = int(input("Invalid amount, Enter volume of first jug (> 1): "))
    jugs.append(temp)

    temp = int(input("Enter volume of second jug (> 1): "))
    while temp < 1:
        temp = int(input("Invalid amount, Enter volume of second jug (> 1): "))
    jugs.append(temp)

    return jugs


def get_goal(jugs):
    """Accepts the desired amount of water as an input from the user.

    Attributes:
        jugs (list): list of two integers representing volumes of the jugs.

    Returns:
        goal (int): the desired amount of water as goal.
    """

    max_vol = max(jugs)

    while True:
        try:
            goal = int(input(f"Enter the goal volume of water (1-{max_vol}): "))
            if goal in range(1, max_vol+1):
                return goal
            else:
                raise ValueError
        except ValueError:
            print("Invalid amount, enter a valid goal amount.")


def is_goal(path, goal):
    """Checks whether the given path matches the goal node.

    Attributes:
        path (list): list of nodes representing the path to be checked.
        goal (int): represents the desired amount of water.
    """

    return path[-1][0] == goal


def been_there(node, check_dict):
    """Validates whether the given node is already visited.

    Attributes:
        node (list): list of two integers representing current state of the jugs.
        check_dict (dict): dictionary storing visited nodes.

    Returns:
        bool: True if node has been visited, otherwise False.
    """

    return check_dict.get(get_index(node), False)


def next_transitions(jugs, path, check_dict):
    """Returns the list of all possible transitions.

    Attributes:
        jugs (list): list of two integers representing volumes of the jugs.
        path (lsit): list of nodes represeting the current path.
        check_dict (dict): dictionary storing visited nodes.

    Returns:
        result (list): list of all possible transistions.
    """

    result = []
    next_nodes = []
    node = []

    a_max = jugs[0]
    b_max = jugs[1]

    a = path[-1][0]
    b = path[-1][1]

    # operations used in Water Jug problem
    # 1. fill in the first jug
    node.append(a_max)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 2. fill in the second jug
    node.append(a)
    node.append(b_max)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 3. second jug to first jug
    node.append(min(a_max, a + b))
    node.append(b - (node[0] - a))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 4. first jug to second jug
    node.append(min(a + b, b_max))
    node.insert(0, a - (node[0] - b))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 5. empty first jug
    node.append(0)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 6. empty second jug
    node.append(a)
    node.append(0)
    if not been_there(node, check_dict):
        next_nodes.append(node)

    # create a list of next paths
    for i in range(0, len(next_nodes)):
        temp = list(path)
        temp.append(next_nodes[i])
        result.append(temp)

    return result


def transition(old, new, jugs):
    """Returns a string explaining the transition from old state/node to new state/node

    Attributes:
        old (list): list representing old state/node.
        new (list): list representing new state/node.
        jugs (list): list of two integers representing volumes of the jugs.
    """

    a = old[0]
    b = old[1]

    a_prime = new[0]
    b_prime = new[1]

    a_max = jugs[0]
    b_max = jugs[1]

    if a > a_prime:
        if b == b_prime:
            return "Clear {0}-liter jug:\t\t\t".format(a_max)
        else:
            return "Pour {0}-liter jug into {1}-liter jug:\t".format(a_max, b_max)
    else:
        if b > b_prime:
            if a == a_prime:
                return "Clear {0}-liter jug:\t\t\t".format(b_max)
            else:
                return "Pour {0}-liter jug into {1}-liter jug:\t".format(b_max, a_max)
        else:
            if a == a_prime:
                return "Fill {0}-liter jug:\t\t\t".format(b_max)
            else:
                return "Fill {0}-liter jug:\t\t\t".format(a_max)


def print_path(path, jugs):
    """Prints the goal path.

    Attributes:
        path (list): list of nodes representing the goal path.
        jugs (list): list of two integers representing volumes of the jugs.
    """

    print("Starting from:\t\t\t\t", path[0])
    for i in range(0, len(path) - 1):
        print(i+1, ":", transition(path[i], path[i+1], jugs), path[i+1])


def search(starting_node, jugs, goal_amount, check_dict):
    """Searches for a path between starting node and goal node.

    Attributes:
        starting_node (list): list of two integers representing initial state of the jugs.
        jugs (list): list of two integers representing volumes of the jugs.
        goal_amount (int): represts the desired amount.
        check_dict (dict): dictionary storing visited nodes.
    """

    print("\nBFS implementation starting...", end="")

    goal = []
    accomplished = False

    q = deque()
    q.appendleft(starting_node)

    while len(q) != 0:
        path = q.popleft()
        check_dict[get_index(path[-1])] = True

        if is_goal(path, goal_amount):
            accomplished = True
            goal = path
            break

        next_moves = next_transitions(jugs, path, check_dict)
        for i in next_moves:
                q.append(i)

    if accomplished:
        print("THE GOAL IS ACHIEVED!\n")
        print_path(goal, jugs)
    else:
        print("Problem cannot be solved. Try different parameters.\n")


if __name__ == '__main__':
    # setting initial state as empty (0,0)
    starting_node = [[0, 0]]

    # getting volumes of both the jugs
    vol_of_jugs = get_vol()

    # getting the goal amount
    goal_amount = get_goal(vol_of_jugs)

    # mainting a dictionary to keep track of visited states
    check_dict = {}
    
    # performing BFS to find path
    search(starting_node, vol_of_jugs, goal_amount, check_dict)
