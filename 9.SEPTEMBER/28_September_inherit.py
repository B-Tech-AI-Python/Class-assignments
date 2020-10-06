# parent/base class
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)

# derived class - simple inheritance
class Teacher(Person):
    
    def __init__(self,name,age,subject):
        Person.__init__(self,name,age)
        self.subject = subject
    
    def displayTeach(self):
        Person.display(self)
        print("Subject is:",self.subject)

# derived class - simple inheritance
class Student(Person):
    
    def __init__(self,name,age,course):
        Person.__init__(self,name,age)
        self.course = course
    
    def display(self):
        Person.display(self)
        print("Course is:",self.course)

# derived class - multilevel inheritance
class SportsStudent(Student):
    
    def __init__(self,name,age,course,sport):
        Student.__init__(self,name,age,course)
        self.sport = sport
    
    def display(self):
        Student.display(self)
        print("Sport is:",self.sport)

p = Person("person", 21)
t = Teacher("teacher", 30, "AI")
s = Student("student", 18, "AI")
ss = SportsStudent("sports student", 19, "AI", "football")

print("\n---Person class---")
p.display()

print("\n\n---Teacher class---")
t.display()
print()
t.displayTeach()

print("\n\n---Student class---")
s.display()

print("\n\n---Sport student class---")
ss.display()





















