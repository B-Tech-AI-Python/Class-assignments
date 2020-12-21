# WAP to generate first n Fibonacci number and factorial of n using functions

def fibonacci(n):
    num_1 = 0
    num_2 = 1

    if (n < 1):
        return

    print(num_1, end=" ")
    for i in range(1, n):
        print(num_2, end=" ")
        next = num_1 + num_2
        num_1 = num_2
        num_2 = next


def factorial(num):
    if num in (0, 1):
        return 1
    else:
        return num * factorial(num-1)


print("1. Factorial")
print("2. Fibonacci")
choice = int(input("What do you want to do? 1 or 2: "))

if choice == 1:
    number = int(input("\nEnter number for factorial: "))
    print(f"Factorial of {number} is {factorial(number)}")

else:
    terms = int(input("\nEnter number of terms: "))
    print("Fibonacci Sequence")
    fibonacci(terms)
