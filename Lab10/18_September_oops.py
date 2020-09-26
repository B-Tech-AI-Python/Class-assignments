# student class
class Student:
    
    def __init__(self, name, roll_num, age=19):
        self.name = name
        self.roll_num = roll_num
        self.age = age
        self.course = "Artificial Intelligence"
    
    def details(self):
        print(f"Name of student: {self.name}")
        print(f"Roll number of student: {self.roll_num}")
        print(f"Age of student: {self.age}")
        print(f"Course of student: {self.course}")
        
    def random(self,x):
        self.x = x

print()
ishani = Student("Ishani", "A023119819004",19)
print(ishani.name)
print(ishani.roll_num)
print(ishani.age)
print(ishani.course)

print()
ishani.details()

print()
ishani.random(10)
print(ishani.x)

print("-------------------------------------------")

x = Student("X", "A023119819002",19)
print(x.name)
print(x.roll_num)
print(x.age)
print(x.course)

print()
x.details()

print()
x.random(50)
print(x.x)

print("-------------------------------------------")

# %%
class Demo:
    x = 0

    def func(self,y):
              
        self.x = y

print()
obj = Demo()
print(obj.x)

obj.func(10)
print(obj.x)

# %% student class
class Student:
    
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num
        self.course = "Artificial Intelligence"
    
    def details(self):
        print(f"Name of student: {self.name}")
        print(f"Roll number of student: {self.roll_num}")
        print(f"Course of student: {self.course}")
        

class SportsStudents(Student):
    
    def __init__(self, name, roll_num, height = 160, weight = 55):
        Student.__init__(self, name, roll_num)
        self.height = height
        self.weight = weight
    
    def details(self):
        print(f"Name of student: {self.name}")
        print(f"Roll number of student: {self.roll_num}")
        print(f"Height of student: {self.height} cm")
        print(f"Weight of student: {self.weight} kg")

ishani = SportsStudents("ishani", "A023119819004")
ishani.details()
































