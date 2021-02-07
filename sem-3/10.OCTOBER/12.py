# container
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return self.pay*12 + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary = Salary(pay,bonus)
    
    def total_salary(self):
        return self.salary.annual_salary()
    
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Total salary:",self.total_salary())

emp = Employee("One", 25, 5, 40)
emp.display()

