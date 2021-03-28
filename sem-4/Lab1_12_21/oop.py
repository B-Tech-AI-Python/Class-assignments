from random import sample

numbers = '0123456789'


class Bank:

    def __init__(self, name, balance=0):

        self.name = name
        self.balance = balance
        self.acc_no = name[0:3].upper() + "".join(sample(numbers, 5))

    def deposit(self, money):

        self.balance += money
        print(f"Your current balance is: {self.balance}")

    def withdraw(self, money):

        if money <= self.balance:
            self.balance -= money
        else:
            print(f"Not enough money to withdraw {money}")
            print(f"Your current balance is: {self.balance}")


user = Bank(input("Enter your name: "), 10000)

print("Name:", user.name)
print("Account number:", user.acc_no)

while True:
    print("\nWhat do you want to do today?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            deposit = int(input("Enter deposit: "))
            user.deposit(deposit)

        elif choice == 2:
            withdraw = int(input("Enter withdraw: "))
            user.withdraw(withdraw)

        elif choice == 3:
            print("Your current balance is:", user.balance)

        elif choice == 4:
            break

        else:
            print("Invalid input! Number should be between 1 and 4!")

    except:
        print("Invalid input! Input should be a number!")
