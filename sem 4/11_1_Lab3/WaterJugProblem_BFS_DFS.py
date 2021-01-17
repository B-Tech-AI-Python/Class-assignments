import collections


def get_index(node):
    """Returns a key value for a given node.

    Attributes:
        Node (list): list of two integers representing current state of the jugs.
    """

    return pow(7, node[0]) * pow(5, node[1])


def get_search_type():
    """Accepts an input for asking the choice for type of searching required i.e. BFS or DFS.

    Returns:
        bool: True for BFS, False otherwise.
    """

    s = input("Enter 'b' for BFS, 'd' for DFS: ").lower()
    while s not in ('b', 'd'):
        s = input(
            "The input is not valid! Enter 'b' for BFS, 'd' for DFS: ").lower()

    return s == 'b'


def get_jugs():
    """Accept volumes of the jugs as an input from the user.

    Reuturns:
        jugs (list): list of two integeres representing volumes of the jugs.
    """

    print("Receiving the volume of the jugs...")
    jugs = []

    temp = int(input("Enter first jug volume (>1): "))
    while temp < 1:
        temp = int(input("Enter a valid amount (>1): "))
    jugs.append(temp)

    temp = int(input("Enter second jug volume (>1): "))
    while temp < 1:
        temp = int(input("Enter a valid amount (>1): "))
    jugs.append(temp)

    return jugs


def get_goal(jugs):
    """Accepts the desired amount of water as an input from the user.

    Attributes:
        jugs (list): list of two integers representing volumes of the jugs.

    Returns:
        goal_amount(int): the desired amount of water as goal.
    """

    print("Receiving the desired amount of the water...")
    max_amount = max(jugs)

    s = "Enter the desired amount of water (1 - {0}): ".format(max_amount)
    goal_amount = int(input(s))

    while goal_amount not in range(1, max_amount+1):
        goal_amount = int(
            input("Enter a valid amount (1 - {0}): ".format(max_amount)))

    return goal_amount


def is_goal(path, goal_amount):
    """Checks whether the given path matches the goal node.

    Attributes:
        path (list): list of nodes representing the path to be checked.
        goal_amount (int): represents the desired amount of water.
    """

    print("Checking if the goal is achieved...")

    return path[-1][0] == goal_amount


def been_there(node, check_dict):
    """Validates whether the given node is already visited.

    Attributes:
        node (list): list of two integers representing current state of the jugs.
        check_dict (dict): dictionary storing visited nodes.
    """

    print("Checking if {0} is visited before...".format(node))

    return check_dict.get(node[0], False)


def next_transitions(jugs, path, check_dict):
    """Returns the list of all possible transitions.

    Attributes:
        jugs (list): list of two integers representing volumes of the jugs.
        path (lsit): list of nodes represeting the current path.
        check_dict (dict): dictionary storing visited nodes.

    Returns:
        result (list): list of all possible transistions.
    """

    print("Finding next transitions and checking for the loops...")

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
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)

    # create a list of next paths
    for i in range(0, len(next_nodes)):
        temp = list(path)
        temp.append(next_nodes[i])
        result.append(temp)

    if len(next_nodes) == 0:
        print("No more unvisited nodes...\nBacktracking...")
    else:
        print("Possible transitions: ")
        for nnode in next_nodes:
            print(nnode)

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


def search(starting_node, jugs, goal_amount, check_dict, is_breadth):
    """Searches for a path between starting node and goal node.

    Attributes:
        starting_node (list): list of two integers representing initial state of the jugs.
        jugs (list): list of two integers representing volumes of the jugs.
        goal_amount (int): represts the desired amount.
        check_dict (dict): dictionary storing visited nodes.
        is_breadth (bool): if True, implements BFS, else DFS.
    """

    if is_breadth:
        print("Implementing BFS...")
    else:
        print("Implementing DFS...")

    goal = []
    accomplished = False

    q = collections.deque()
    q.appendleft(starting_node)

    while len(q) != 0:
        path = q.popleft()
        check_dict[get_index(path[-1])] = True

        if len(path) >= 2:
            print(transition(path[-2], path[-1], jugs), path[-1])

        if is_goal(path, goal_amount):
            accomplished = True
            goal = path
            break

        next_moves = next_transitions(jugs, path, check_dict)
        for i in next_moves:
            if is_breadth:
                q.append(i)
            else:
                q.appendleft(i)

    if accomplished:
        print("The goal is achieved\nPrinting the sequence of the moves...\n")
        print_path(goal, jugs)
    else:
        print("Problem cannot be solved.")


if __name__ == '__main__':
    starting_node = [[0, 0]]

    jugs = get_jugs()

    goal_amount = get_goal(jugs)

    check_dict = {}

    is_breadth = get_search_type()

    search(starting_node, jugs, goal_amount, check_dict, is_breadth)
