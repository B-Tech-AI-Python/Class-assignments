from time import time
from queue import PriorityQueue


class Puzzle:
    # Setting the goal state of 8-puzzle
    goal_state = [1,2,3,8,0,4,7,6,5]
    # Setting up the members of a class
    heuristic = None
    evaluation_function = None
    needs_hueristic = False
    num_of_instances = 0

    def __init__(self, state, parent, action, path_cost, needs_hueristic=False):
        self.parent = parent
        self.state = state
        self.action = action
        #TODO: calculate the path_cost as the sum of its parent cost and path_cost
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
    
    # method used to display a state of 8-puzzle
    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    # method used to generate a heuristic value
    def generate_heuristic(self):
        self.heuristic = 0
        for num in range(1,9):
            # calculate the heuristic value as manhattan distance which is the absolute 
            # difference between current state and goal state. 
            # Use index() method to get the index of num in state
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / 3)
            j = int(distance % 3)
            self.heuristic = self.heuristic + i + j

    def goal_test(self):
        # include a condition to compare the current state with the goal state
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i,j):
        # find the legal actions as Up, Down, Left, Right based on each cell of state
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

    #method to generate the child of the current state of the board
    def generate_child(self):
        # create an empty list
        children = []
        x = self.state.index(0)
        #TODO: generate the row (i) & col (j) position based on the current index of 0 on the board 
        i = int(x / 3)
        j = int(x % 3)
        # call the method to find the legal actions based on i and j values
        legal_actions = self.find_legal_actions(i,j)

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
            children.append(Puzzle(new_state, self, action, 1, self.needs_hueristic))

        # return the children
        return children
    
    #method to find the solution
    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution


#method for A-star search
#TODO: pass the initial_state as parameter to the breadth_first_search method
def Astar_search(initial_state):
    count=0
    #TODO: create an empty list of explored nodes
    explored=[]
    #TODO: create a instance of Puzzle as initial_state, None, None, 0, True
    start_node=Puzzle(initial_state, None, None, 0, True)
    q = PriorityQueue()
    #TODO: put a tuple with start_node.evaluation_function, count, start_node into PriorityQueue
    q.put((start_node.evaluation_function, count, start_node))

    while not q.empty():
        #TODO: get the current node of a queue. Use the get() method of Queue
        node=q.get()
        #TODO: extract the current node of a PriorityQueue based on the index of a tuple. 
        #Refer a tuple format put in PriorityQueue  
        node=node[2]
        #TODO: Append the state of node in the explored list as node.state
        explored.append(node.state)
        if node.goal_test():
            return node.find_solution()
        #TODO: call the generate_child method to generate the child node of current node
        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                #TODO: put a tuple with child.evaluation_function, count, child into PriorityQueue
                q.put((child.evaluation_function, count, child))
    return


# Start executing the 8-puzzle with setting up the initial state
# Here we have considered 3 initial state intitalized using state variable
state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]
#Iterate over number of initial_state
for i in range(0,3):
    # Initialize the num_of_instances to zero
    Puzzle.num_of_instances = 0
    # Set t0 to current time
    t0 = time()
    astar = Astar_search(state[i])
    # Get the time t1 after executing the breadth_first_search method
    t1 = time() - t0
    print('A*:',astar)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()
    print('------------------------------------------')

# Show the path in traversing the A-star algorithm of each state from intial_state to goal state.

