# employee class
class Employee:
    count = 0
    
    def __init__(self, name, designation, salary):
        Employee.count += 1
        
        self.name = name
        self.designation = designation
        self.__salary = salary
    
    def display(self):
        print(f"{self.name} - {self.designation}")
    
    def salaryDisplay(self):
        print(f"Salary if {self.name} is {self.__salary}")
        
# display employee count
def employeeCount():
    print("\nThe number of employees in the organisation are:",Employee.count)

emp1 = Employee(input("Enter name: "), input("Enter desgination: "), int(input("Enter salary: ")))
emp1.display()

emp2 = Employee(input("Enter name: "), input("Enter desgination: "), int(input("Enter salary: ")))
emp2.display()

employeeCount()
# %%
class Circle:
    pi = 3.1416
    
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        temp = Circle.pi*(self.radius**2)
        print("Area of circle is {:.2f}".format(temp))
        
    def circumference(self):
        temp = 2*Circle.pi*self.radius
        print("Circumference of circle is {:.2f}".format(temp))

rad = int(input("Enter radius: "))
cir1 = Circle(rad)
cir1.area()
cir1.circumference()

# %%
class Fraction:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def value(self):
        temp = self.numerator / self.denominator
        print("\nValue of fraction")
        print(f"{self.numerator} / {self.denominator} = {temp}")

numerator = int(input("Enter numerator: "))

while True:
    denominator = int(input("Enter denominator: "))
    if denominator > 0:
        break
    else:
        print("Value of denominator should be greater than 0!")
        print("Try again!")

frac1 = Fraction(numerator, denominator)
frac1.value()

# %%
class Numbers:
    
    def __init__(self, nums):
        self.nums = nums
    
    def maximum(self):
        print(f"Max value in the list is: {max(self.nums)}")

nums = list(int(x) for x in input("Enter list of numbers: ").split())
obj1 = Numbers(nums)
obj1.maximum()

# %%
class Banking:
    
    accNum = 0
    
    def __init__(self, name, balance = 0):
        Banking.accNum += 1
        
        self.name = name
        self.accNum = Banking.accNum
        self.balance = balance
    
    def checkBalance(self):
        print(f"Your current balance is: {self.balance}")
        
    def deposit(self, money):
        
        self.balance += money
        Banking.checkBalance(self)
    
    def withdraw(self, money):
        
        if money <= self.balance:        
            self.balance -= money
            Banking.checkBalance(self)
        else:
            print(f"Not enough money to withdraw {money}")
            Banking.checkBalance(self)


p1 = Banking("Person One", 10000)

while True:
    try:
        print("\nDo you want to deposit, withdraw or check balance?")
        print("1.Deposit\n2.Withdraw\n3.Check balance")
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            deposit = int(input("Enter deposit: "))
            p1.deposit(deposit)
            
        elif choice == 2:
            withdraw = int(input("Enter withdraw: "))
            p1.withdraw(withdraw)
        
        elif choice == 3:
            p1.checkBalance()
        
        switch = input("Do you want to deposit or withdraw again? y or n: ")
        if switch.lower().startswith("y"):
            continue
        else:
            break

    except:
        print("Invalid input! Try again!")

# %%
class Store:

    items = {}

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

        Store.items[self.code] = [self.name, self.price]

Book = Store("Book", 1, 100)
Pen = Store("Pen", 2, 30)
Eraser = Store("Eraser", 3, 10)
Glue = Store("Glue", 4, 55)

print("\n--------Products--------")
print("Code   Item       Price")

for key, values in Store.items.items():
    print(" ",key,end="    ")
    print(values[0],end=" "*(12-len(values[0])))
    print(values[1])

sold = dict()

print("\nWhich item do you want to buy?", end="")
while True:
    buy = int(input("Enter code: "))
    if buy in Store.items:
        quantity = int(input("Enter quantity of items you want: "))
        if buy in sold:
            sold[buy][1] += Store.items[buy][1]*quantity
        else:
            sold[buy] = [Store.items[buy][0], Store.items[buy][1], quantity, Store.items[buy][1]*quantity]

        choice = input("Do you want any more items? y or n: ")
        if choice.lower().startswith("y"):
            continue
        else:
            break

    else:
        print("Invalid input! Try again!")

print("\n-------------------Bill------------------")
print("Code   Item     Price    Quantity   Total")

for key, values in sold.items():
    print(" ",key,end="    ")
    print(values[0],end=" "*(10-len(values[0])))
    print(values[1],end=" "*(10-len(str(values[1]))))
    print(values[2],end=" "*(10-len(str(values[2]))))
    print(values[3])

total = 0
for value in sold.values():
    total += value[3]

print("\nTotal price:",total)
