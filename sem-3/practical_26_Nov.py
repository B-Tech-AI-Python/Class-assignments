"""Multiple Inheritance program."""


class Animal():
    """Animal class.
    
    Args:
        habitat (str): Type of place the animal is found.

    """

    def __init__(self, habitat):
        """Constructor of Animal class."""

        self.habitat = habitat
        print("---An Animal---")


class Mammal():
    """Mammal class.
    
    Args:
        fur (bool): If the mammal has fur.
        food (str): Type of food the mammal eats.

    """

    def __init__(self, food, fur):
        """Constructor of Mammal class."""

        self.food = food
        self.fur = fur
        print("---A Mammal---")


class Human(Animal, Mammal):
    """Human class.
    
    Args:
        age (int): Age of the human.
        sex (str): Sex of the human.

    """

    def __init__(self, age, sex, habitat, food, fur=False):
        """Constructor of Human class."""

        Animal.__init__(self, habitat)
        Mammal.__init__(self, food, fur)

        self.age = age
        self.sex = sex

        print("---A Human---")

    def display(self):
        """Display method to print the different characteristics."""

        print(f"\nAge: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Habitat: {self.habitat}")
        print(f"Food: {self.food}")
        print(f"Fur: {self.fur}\n")


class Panda(Animal, Mammal):
    """Panda class.
    
    Args:
        age (int): Age of the panda.
        sex (str): Sex of the panda.

    """

    def __init__(self, age, sex, habitat, food, fur=True):
        """Constructor of Panda class."""

        Animal.__init__(self, habitat)
        Mammal.__init__(self, food, fur)

        self.age = age
        self.sex = sex

        print("---A Panda---")

    def display(self):
        """Display method to print the different characteristics."""

        print(f"\nAge: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Habitat: {self.habitat}")
        print(f"Food: {self.food}")
        print(f"Fur: {self.fur}\n")


person1 = Human(19, 'Female', 'Land', 'Omnivore')
person1.display()

panda1 = Panda(10, 'Female', 'Forests', 'Herbivore')
panda1.display()
