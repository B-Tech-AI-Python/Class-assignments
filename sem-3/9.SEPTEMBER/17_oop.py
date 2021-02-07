# bank
class Banking:
    
    def __init__(self, name, balance = 0):
        
        self.name = name
        self.balance = balance
        
    def deposit(self, money):
        
        self.balance += money
        print(f"Your current balance is: {self.balance}")
    
    def withdraw(self, money):
        
        if money <= self.balance:        
            self.balance -= money
        else:
            print(f"Not enough money to withdraw {money}")
            print(f"Your current balance is: {self.balance}")


ishani = Banking("Ishani", 10000)
print(ishani)
print(ishani.name)
print(ishani.balance)

deposit = int(input("Enter deposit: "))
ishani.deposit(deposit)

withdraw = int(input("Enter withdraw: "))
ishani.withdraw(withdraw)

