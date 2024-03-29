# Import the necessary libraries
from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

# Declares a type variable V as variable type and D as domain type
V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V, D], ABC):
    """Base class for all constraints."""

    def __init__(self, variables: List[V]) -> None:
        """Constructor fot the Constraint class."""
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        """Abstract method which must be overridden by subclasses."""
        ...


class CSP(Generic[V, D]):
    """A constraint satisfaction problem consists of variables of type V
    that have ranges of values known as domains of type D and constraints
    that determine whether a particular variable's domain selection is valid.
    """

    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        """Constructor for CSP class."""

        # variables to be constrained
        self.variables: List[V] = variables
        # domain of each variable
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}

        for variable in self.variables:
            self.constraints[variable] = []

            if variable not in self.domains:
                raise LookupError(
                    "Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        """This method adds constraint to variables as per their domains."""

        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        """Check if the value assignment is consistent.

        Checks if the value assignment is consistent by checking
        all constraints for the given variable against it.
        """

        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        """This method is performing the backtracking search to find the result."""

        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [
            v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        # Iterate over self.domains[first]
        for value in self.domains[first]:
            local_assignment = assignment.copy()

            # Assign the value
            local_assignment[first] = value

            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                # recursively call the self.backtracking_search method based on the local_assignment
                result: Optional[Dict[V, D]] = self.backtracking_search(
                    local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None


class MapColoringConstraint(Constraint[str, str]):
    """MapColoringConstraint is a subclass of Constraint class."""

    def __init__(self, place1: str, place2: str) -> None:
        """Constructor for MapColoringConstraint."""
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        """Abstract method satisfied in subclass."""

        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        return assignment[self.place1] != assignment[self.place2]


class SendMoreMoneyConstraint(Constraint[str, int]):
    """SendMoreMoneyConstraint is a subclass of Constraint class."""

    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # if there are duplicate values then it's not a solution
        if len(set(assignment.values())) < len(assignment):
            return False

        # if all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            s: int = assignment["S"]
            e: int = assignment["E"]
            n: int = assignment["N"]
            d: int = assignment["D"]
            m: int = assignment["M"]
            o: int = assignment["O"]
            r: int = assignment["R"]
            y: int = assignment["Y"]
            send: int = s * 1000 + e * 100 + n * 10 + d
            more: int = m * 1000 + o * 100 + r * 10 + e
            money: int = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True  # no conflict


class CrossRoadsDanger(Constraint[str, int]):
    """CrossRoadsDanger is a subclass of Constraint class."""

    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # if there are duplicate values then it's not a solution
        if len(set(assignment.values())) < len(assignment):
            return False

        # if all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            c: int = assignment["C"]
            r: int = assignment["R"]
            o: int = assignment["O"]
            s: int = assignment["S"]
            a: int = assignment["A"]
            d: int = assignment["D"]
            n: int = assignment["N"]
            g: int = assignment["G"]
            e: int = assignment["E"]

            cross: int = c * 10000 + r * 1000 + o * 100 + s * 10 + s
            roads: int = r * 10000 + o * 1000 + a * 100 + d * 10 + s
            danger: int = d * 100000 + a * 10000 + n * 1000 + g * 100 + e * 10 + r
            return cross + roads == danger
        return True  # no conflict


print("1. Map Coloring Constraint for pic 1")
print("2. Map Coloring Constraint for pic 2")
print("3. Send More Money")
print("4. Cross Roads Danger")
print("5. Exit")

while True:
    choice = int(input("\n\nWhat would you like to do? 1-5: "))

    # MAP COLORING 1
    if choice == 1:
        variables: List[str] = ["BOX_1", "BOX_2", "BOX_3", "BOX_4",
                                "BOX_5", "BOX_6", "BOX_7"]

        domains: Dict[str, List[str]] = {}
        for variable in variables:
            domains[variable] = ["red", "green", "blue"]

        csp: CSP[str, str] = CSP(variables, domains)

        csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_2"))
        csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_4"))
        csp.add_constraint(MapColoringConstraint("BOX_4", "BOX_2"))
        csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_2"))
        csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_4"))
        csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_5"))
        csp.add_constraint(MapColoringConstraint("BOX_5", "BOX_4"))
        csp.add_constraint(MapColoringConstraint("BOX_6", "BOX_4"))
        csp.add_constraint(MapColoringConstraint("BOX_6", "BOX_5"))
        csp.add_constraint(MapColoringConstraint("BOX_6", "BOX_7"))

        solution: Optional[Dict[str, str]] = csp.backtracking_search()

        if solution is None:
            print("No solution found!")
        else:
            print(solution)

    # MAP COLORING 2
    elif choice == 2:
        variables: List[str] = ["BOX_1", "BOX_2", "BOX_3",
                                "BOX_4"]

        domains: Dict[str, List[str]] = {}
        for variable in variables:
            domains[variable] = ["red", "green"]

        csp: CSP[str, str] = CSP(variables, domains)

        csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_2"))
        csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_3"))
        csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_4"))
        csp.add_constraint(MapColoringConstraint("BOX_2", "BOX_3"))
        csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_4"))

        solution: Optional[Dict[str, str]] = csp.backtracking_search()

        if solution is None:
            print("No solution found!")
        else:
            print(solution)

    # SEND MORE MONEY
    elif choice == 3:
        letters: List[str] = ["S", "E", "N", "D", "M", "O", "R", "Y"]
        possible_digits: Dict[str, List[int]] = {}

        for letter in letters:
            possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        possible_digits["M"] = [1]  # so we don't get answers starting with a 0

        csp: CSP[str, int] = CSP(letters, possible_digits)

        csp.add_constraint(SendMoreMoneyConstraint(letters))

        solution: Optional[Dict[str, int]] = csp.backtracking_search()

        # Print solution
        if solution is None:
            print("No solution found!")
        else:
            print(solution)

    # CROSS RAODS DANGER
    elif choice == 4:
        letters: List[str] = ["C", "R", "O", "S", "A", "D", "N", "G", "E"]
        possible_digits: Dict[str, List[int]] = {}

        for letter in letters:
            possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        possible_digits["D"] = [1]  # so we don't get answers starting with a 0

        csp: CSP[str, int] = CSP(letters, possible_digits)

        csp.add_constraint(CrossRoadsDanger(letters))

        solution: Optional[Dict[str, int]] = csp.backtracking_search()

        # Print solution
        if solution is None:
            print("No solution found!")
        else:
            print(solution)

    # EXIT
    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try Again")
