# multilevel - teacher hod
class Person:
    def name(self):
        print("Name is ")

class Teacher(Person):
    def qualification(self):
        print("Qualification: Phd required")

class HOD(Teacher):
    def experience(self):
        print("Experience should be more than 15 years.")

H = HOD()
H.name()
H.qualification()
H.experience()

# %% multilevel - student scholar
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        print("Name is ")

class Student(Person):
    def __init__(self, name, age, rollNo, marks):
        Person.__init__(self, name, age)
        self.rollNo = rollNo
        self.marks = marks
    
    def display(self):
        print("\n\nName:",self.name)
        print("Age:",self.age)
        print("Roll number:",self.rollNo)
        print("Marks:",self.marks)
        print()

class Scholar(Student):
    def scholarCheck(self):
        if self.marks in range(95,101):
            self.display()
            print("Scholarship of 100%")
        
        elif self.marks in range(90,95):
            self.display()
            print("Scholarship of 90%")
        
        elif self.marks in range(85,90):
            self.display()
            print("Scholarship of 80%")
        
        else:
            self.display()
            print("No scholarship!")

stu1 = Scholar("One", 19, 1, 97)
stu2 = Scholar("Two", 18, 2, 93)
stu3 = Scholar("Three", 20, 3, 86)
stu4 = Scholar("Four", 19, 4, 84)

stu1.scholarCheck()
stu2.scholarCheck()
stu3.scholarCheck()
stu4.scholarCheck()

# %% multipath
class Student:
    def name(self):
        print("Name is ")

class Performance(Student):
    def marks(self):
        print("Above 70%")

class Sports(Student):
    def sportType(self):
        print("Basketball")

class Result(Performance, Sports):
    def eligible(self):
        self.marks()
        self.sportType()

obj1 = Result()
obj1.eligible()

