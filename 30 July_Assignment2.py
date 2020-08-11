# Greatest common divisor
import time
print("---Greatest common divisor---")


def gcd(x, y):

    for num in range(1, max(x, y)+1):
        if x % num == 0 and y % num == 0:
            gcd = num
    return gcd


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"\nThe greatest common divisor of {num1} and {num2} is {gcd(num1,num2)}")

# %% exponential
print()
print("---Exponential---")


def power(base, exp):
    if(exp == 1):
        return(base)
    else:
        return (base*power(base, exp-1))


base = int(input("Enter base: "))
exp = int(input("Enter the exponential value: "))
print("\nResult:", power(base, exp))

# %%  fibonacci series
print()
print("---Fibonacci series---")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


while True:
    try:
        terms = int(input("Enter number of terms you want in your fibonacci series: "))
        if isinstance(terms, int):
            break
        else:
            raise ValueError

    except ValueError:
        print("INVALID INPUT!")

if terms <= 0:
    print("Plese enter a positive integer")
else:
    print("\nFibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
print()

# %% to find the number of times a recursive function is called
print()
print("---The number of times a recursive function is called---")


def fact(num, count=1):
    print("Function counter:", end=" ")
    print(count)
    return num * fact(num-1, count+1) if num > 1 else 1


num = int(input("You want the factorial of: "))
print()
result = fact(num)
print("\nYour factorial is:", result)

# %% concatenate two strings using recursion
print()
print("---Concatenation---")


def concatenate(string):
    pass


string1 = input("Enter your first string: ")
string2 = input("Enter your second string: ")


# %%  menu driven program using functions to perform calculator operations
def calc(choice, num1, num2):
    if choice == 1:
        return num1+num2
    elif choice == 2:
        return num1-num2
    elif choice == 3:
        return num1*num2
    elif choice == 4:
        return num1/num2
    else:
        pass


print()
print("---CALCULATOR---")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        choice = float(input("What operation would you like to perform? "))
        if isinstance(choice, float) and isinstance(num1, float) and isinstance(num2, float):
            if choice in range(1, 5):
                print("Answer:", calc(choice, num1, num2))
                break
            else:
                print("INVALID!\nEnter a choice between 1-4!")
        else:
            raise ValueError

    except ValueError:
        print("INVALID INPUT!")

# %% lambda function to find smallest number
print()
print("---Smallest number---")
def small(x, y): return print("\nThey are equal!") if x == y else print(
    "\nThe smaller number is", min(x, y))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
small(num1, num2)

# %% to compute lambda(n) for all positive values of n
time.sleep(1)
print()
print("---Recursive lambda---")
def func(x): return 1 if x < 1 else func(x/2) + 1


for num in range(1000):
    print(func(num), end=" ")
