# Area of circle
import math
r = int(input("Enter radius of circle: "))

a = math.pi*r*r
print("Area of circle is: ", a)

# %%
# Area of triangle
h = int(input("Enter height of triangle: "))
b = int(input("Enter bas of triangle: "))

a = 0.5*h*b
print("Area of triangle is: ", a)

# %%
# Calculate distance between 2 points
print("Enter co-ordinates of point 1")
x1, y1 = int(input("x1: ")), int(input("y1: "))

print("Enter co-ordinates of point 2")
x2, y2 = int(input("x2: ")), int(input("y2: "))

d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print("Distance between the 2 points is: ", d)

# %%
# Calculate bill amount for an item
quantity = int(input("Enter quantity of items sold: "))
price = int(input("Enter price of item bought: "))
discount = int(input("Enter discount percent on the item: "))
tax = int(input("Enter the tax amount: "))

amount = quantity*price
discount_amt = amount*discount/100
subtotal = amount-discount_amt
tax_amt = subtotal*tax
total = subtotal+tax_amt

print("\n*******Bill*******")
print("Quantity:", quantity)
print("Price per item:", price)
print("Price of items:", amount)
txt = "{:0.0%}"
print("Discount on items:", txt.format(discount/100))
print("Subtotal amount:", subtotal)
print("Tax on items:", tax)
print("After tax:", tax_amt)
print("Total:", total)

# %%
# Calculate a student’s result
print("Enter marks for both examinations")
e1, e2 = int(input("Exam 1: ")), int(input("Exam 2: "))
print("Enter marks for the 3 activities")
a1, a2, a3 = int(input("Activity 1: ")), int(input("Activity 2: ")), int(input("Activity 3: "))
s = int(input("Enter marks for the sports event: "))

exam = (e1 + e2)/2
wtg_exam = 0.5*exam

activity = (a1 + a2 + a3)/3
wtg_activity = 0.3*activity

wtg_sports = 0.2*s

total = wtg_exam + wtg_activity + wtg_sports

txt = "{:0.0%}"

print("\n*******Result*******\n")

print("Exams:", wtg_exam)
print("Activities:", wtg_activity)
print("Sports:", wtg_sports)
print("Total marks:", txt.format(total/100))

# %%
# Read a character in uppercase and then print it in lowercase
x = input("Enter uppercase character: ")
print(x.lower())

# %%
# Swapping 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a, b)

t = a
a = b
b = t

print(a, b)

# %%
# calculate number of seconds in a day
print("Number of hours in a day: 24")
print("Number of minutes in an hour: 60")
print("Number of seconds in a minute: 60")
total = 24*60*60
print("Total seconds in a day are:\n24*60*60 =", total, "seconds")

# %%
# Momentum
m = int(input("Enter mass (in kilograms): "))
c = int(input("Enter velocity (in metre/second): "))

e = m*(c**2)

print("\nMomentum is=", e)
