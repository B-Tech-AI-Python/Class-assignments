# %%
# Average of n natural numbers

import calendar
n = int(input("Enter range: "))
sum = 0

for n in range(n+1):
    sum = sum+n

avg = sum/n
print("Average is:", avg)

# %%
# Factorial of a number
n = int(input("Enter a number: "))

fact = 1

if n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        fact = fact*i
    print("The factorial is:", fact)

# %%
# Check if number is prime or not
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if (n % i == 0):
            print(n, "is composite")
            break
    else:
        print(n, "is prime")

elif n == 0 or 1:
    print("Invalid input")
else:
    pass

# %%
# Calculate sum of series
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = (1/i)+sum
print("The sum of the series is:", sum)

# %%
# Generate calendar

yyyy = int(input("Enter year in yyyy format: "))
mm = int(input("Enter month in mm format: "))

print()
print(calendar.month(yyyy, mm))

# %%
# Generate pyramid sequence
n = int(input("Enter rows: "))

for i in range(n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# %%
# Multiplication table till 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i, 'x', j, '=', (i*j))
    print("")
