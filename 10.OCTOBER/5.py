# employee class
class Employee:
    
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

class Display(Employee):
    
    def displayInfo(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
        print()

emp1 = Display("One", "des1", 100)
emp2 = Display("Two", "des2", 200)
emp3 = Display("Three", "des3", 300)
emp4 = Display("Four", "des4", 400)
emp5 = Display("Five", "des5", 500)

emp1.displayInfo()
emp2.displayInfo()
emp3.displayInfo()
emp4.displayInfo()
emp5.displayInfo()

# %% student class
class Student:
    
    def __init__(self, name, rollno):        
        self.name = name
        self.rollno = rollno
    
class Fees(Student):
    
    def __init__(self, name, rollno, fees):
        Student.__init__(self, name, rollno)
        self.fees = fees
    
    def submitFees(self):
        print("\n--------Fees--------")
        print("\tName:", self.name)
        print("\tRoll Number:", self.rollno)
        print("\tFees:", self.fees)
        self.fees = 0
        print("\nYour fees is submitted!\n\n")
    
class Result(Student):
    
    def __init__(self,  name, rollno, marks):
        Student.__init__(self, name, rollno)
        self.marks = dict(marks)
    
    def grade(self):
        for i in self.marks:
            if i in range(91,101):
                self.marks[i] = 'A'

            elif i in range(81,91):
                self.marks[i] = 'B'
            
            elif i in range(71,81):
                self.marks[i] = 'C'
            
            elif i in range(61,71):
                self.marks[i] = 'D'
            
            elif i in range(33,61):
                self.marks[i] = 'E'
            
            elif i in range(33):
                self.marks[i] = 'F'
        
    def display(self):
        print("\n--------Report Card--------")
        print("\tName:", self.name)
        print("\tRoll Number:", self.rollno)
        print("\n\tMarks       Grade")
        for key, value in self.marks.items():
            print("\t", key,"         ",value)

s1 = Fees("s1", "04", 10000)
s1.submitFees()

s1 = Result("s1", "04", {97:1, 85:2, 74:3, 68:4, 51:5, 32:6})
s1.grade()
s1.display()

# %% employee2 class
class Employee:
    
    def __init__(self, name, designation, empno):
        self.name = name
        self.designation = designation
        self.empno = empno

class Qualification(Employee):
    
    def __init__(self, name, designation, empno, ug = None, pg = None, exp = None):
        Employee.__init__(self, name, designation, empno)
        self.ug = ug
        self.pg = pg
        self.exp = exp

class Salary(Qualification, Employee):
    
    def __init__(self, name, designation, empno, ug, pg, exp, salary):
        Qualification.__init__(self, name, designation, empno, ug, pg, exp)
        self.salary = salary
    
    def increment(self):
        if self.ug:
            if self.pg:
                if self.exp:
                    self.salary += 1000
                else:
                    self.salary += 500
            else:
                self.salary += 200
        else:
            pass
        
    def displayInfo(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
        print()

emp = Salary("One", "des1", 10, "B.tech", 'B.tech', '100', 100)
emp.increment()
emp.displayInfo()





















