# modules
import math
import random
import calendar

# %% degrees to radians
print("\n\n----- degrees to radians -----")
input_degree = float(input("Enter value in degrees: "))

print("Your input:",input_degree)

print("Degree to radians:",math.radians(input_degree))

# %% radians to degrees
print("\n\n----- radians to degrees -----")
input_radians = float(input("Enter value in radians: "))

print("Your input:",input_radians)

print("Radians to degrees:",math.degrees(input_radians))

# %% n
print("\n\n----- square of sum - sum of squares -----\n")
n = random.randint(1,9999)

total1 = 0
for i in range(1,n+1):
    total1 += i
total1 = total1**2

total2 = 0
for i in range(1,n+1):
    total2 += i**2

print(f"{total1} - {total2} = {total1-total2}")

# %%
print("\n\n----- number guessing game -----")

chosen_num = random.randint(1,9)

while True:

    try:
        user_input = int(input("Guess a number between 1 and 9: "))
        if isinstance(user_input, int):
            print("Your guess is:",user_input)
            if user_input == chosen_num:
                print("You have guessed the number!!")
                break
            else:
                print("Wrong guess! Try again!")
        else:
            raise ValueError

    except ValueError:
        print("Invalid input! Try again!")

print("Thank you for playing!")

# %%
print("\n\n----- random even numbers -----")

for i in range(1,4):
    while True:
        num = random.randint(1,100)
        if num % 2 == 0:
            print(num)
            break

# %%
print("\n\n----- unique random integers -----")

def randSeq(input_list):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    
    num = random.choice(numbers)
    if num not in input_list:
        input_list.append(num)
    
    return input_list

input_list = list()

for i in range(6):
    input_list = randSeq(input_list)

print(input_list)

# %%
print("\n\n----- calendar -----\n")

month = random.randint(1,12)
year = random.randint(1920,2020)

print(calendar.month(year, month))

# %%
print("\n\n----- time -----")












