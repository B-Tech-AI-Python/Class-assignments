def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


a = int(input("Enter number to find it's factorial: "))
print(f"The factorial of {a} is {factorial(a)}")
