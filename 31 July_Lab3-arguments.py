#Cube of a number
def with_cube(a):
    print(f"Your number is {a}")
    a = a**3
    print(f"Cube of number is {a}")

def without_cube():
    a = int(input("Enter number to calculate cube: "))
    print(f"Number is {a}")
    a = a**3
    print(f"Cube of number is {a}")
    
with_cube(3)
without_cube()

#%%
#Area of a circle
def area():
    rad = int(input("Enter radius of circle:"))
    area = 3.14*rad*rad
    print(f"The area of the given circle is {area}")

area()

#%%
#sum from num1 to num2
def without_sums():
    num1 = int(input("Enter lower limit: "))
    num2 = int(input("Enter upper limit: "))
    x = 0
    for i in range(num1,num2+1):
        x+=i
    print(f"\nSum of numbers from {num1} to {num2} is: {x}")


without_sums()

#%%
def with_sums(num1, num2):
    x = 0
    for i in range(num1,num2+1):
        x+=i
    return x

num1 = int(input("Enter lower limit: "))
num2 = int(input("Enter upper limit: "))
result = with_sums(num2,num1)
print(f"\nSum of numbers is: {result}")

#%%
def kw_sums(int_1, int_2):
    x = 0
    for i in range(int_1,int_2+1):
        x+=i
    return x

num1 = int(input("Enter lower limit: "))
num2 = int(input("Enter upper limit: "))
result = kw_sums(int_2=num2,int_1=num1)
print(f"\nSum of numbers from {num1} to {num2} is: {result}")

#%%
def da_sums(num1=1, num2=10):
    x = 0
    for i in range(num1,num2+1):
        x+=i
    return x

num1 = int(input("Enter lower limit: "))
num2 = int(input("Enter upper limit: "))
result = da_sums(num1,num2)
print(f"\nSum of numbers is: {result}")
