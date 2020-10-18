from datetime import date

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, (date.today().year - year))
    
    @staticmethod
    def isAdult(age):
        if age > 18:
            return "an adult"
        else:
            return "not an adult"

person1 = Person("One", 19)
person2 = Person.fromBirthYear("Two", 2004)

print(f"Age of {person1.name} is {person1.age} and they are {person1.isAdult(person1.age)}.")

print(f"Age of {person2.name} is {person2.age} and they are {person2.isAdult(person2.age)}.")

# %%
class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def totalMarks(self):        
        self.total = sum(self.marks)
    
    def display(self):
        print(self.name,"has the following marks:")
        j = 1
        while j in range(1,len(self.marks)+1):
            for i in self.marks:
                print(f"Marks of subject {j} are {i}")
                j += 1

        print("The total marks are:",self.total)


name = input("Enter name: ")
marks = list(int(x) for x in input("Enter marks separated by space: ").split())

print()
student1 = Student(name,marks)
student1.totalMarks()

student1.display()
