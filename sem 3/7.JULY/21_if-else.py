# Largest out of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a > b):
    print("first number is the largest number")
elif(a < b):
    print("second number is the largest number")
else:
    print("numbers are equal")

# %%
# Smallest out of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a < b):
    print("first number is the smallest number")
elif(a > b):
    print("second number is the smallest number")
else:
    print("numbers are equal")

# %%
# Smallest out of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if((a < b) and (a < c)):
    print("first number is the smallest number")
elif((b < a) and (b < c)):
    print("second number is the smallest number")
elif((c < a) and (c < b)):
    print("third number is the smallest")
else:
    print("there is no one smallest vlaue")

# %%
# Odd/Even
a = int(input("Enter number: "))

if(a % 2 == 0):
    print("number is even")
else:
    print("number is odd")

# %%
# Positive/Negative
a = int(input("Enter number: "))

if(a > 0):
    print("number is positive")
elif(a < 0):
    print("number is the negative")
else:
    print("number is zero")

# %%
# Blood Donation
blood_recipient = input("Enter blood group of recipient: ")
blood_donor = input("Enter blood group of donor: ")

if(blood_recipient == blood_donor):
    print("blood group is a match")
else:
    print("blood group is not a match")
