# Publication
class Publication:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
    
    def __str__(self):
        return f"{self.year}: {self.title} - {self.author}"


# Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Faculty
class Faculty(Person):
    
    publications = []
    
    def __init__(self, name, age):
        Person.__init__(self, name, age)
    
    def pub(self, title, year):
        Faculty.publications.append(Publication(title, year, self.name))

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("\nNumber of publications:",len(Faculty.publications))
        print("Titles of publications:")
        for paper in Faculty.publications:
            print(paper)

f1 = Faculty("One", 25)
f1.pub("Research Paper 1", 2009)
f1.pub("Research Paper 2", 2012)
f1.pub("Research Paper 3", 2013)
f1.pub("Research Paper 4", 2017)

f1.display()

# %%
class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo's __new__() invoked")

    def __init__(self):
        print("Demo's __init__() invoked")

class Derived_Demo(Demo):
    def __new__(self):
        print("Derived_Demo's __new__() invoked")

    def __init__(self):
        print("Derived_Demo's __init__() invoked")



obj1 = Derived_Demo()
obj2 = Demo()

# %%
class Test:
    def __init__(self):
        self.x = 0

class Demo(Test):
    def __init__(self):
        Test.__init__(Demo)
        self.y = 1

b = Demo()
print(b.y)
print(b.x)

# %%
class A():
    def disp(self):
        print("A disp()")

class B(A):
    pass

obj = B()
obj.disp()






































