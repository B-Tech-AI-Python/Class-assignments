#varible number of arguments
def favourites(name, *fave_subjects):
    print(f"Your name is {name}")
    
    print("Your favourite subjects are:")
    
    for i in range(len(fave_subjects)):
        print(i+1, fave_subjects[i])
    
favourites("Ishani","Python","Mathematics", "English", "Data Structures in C")

#%% lambda functions
def addition(*args):
    '''Arguments passed through it are added.'''
    print("The sum of the given numbers are: ",sum(args))

addition(1,2,3,4)

lambda_add = lambda x,y,z : x+y+z
print("The sum of the given numbers using lambda add are: ",lambda_add(4,5,1))

#%% using lambda functions along with defined functions
def sort(*args):
    '''Arguments passed through it are sorted.'''

    print("\nThis is my sorted list of numbers:\n")
    for num in sorted(args):
        print(num, " ", end="")

add = lambda x,y:x+y
diff = lambda x,y:x-y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"The numbers are {x} and {y}")
print(f"Their sum is {x} + {y} = {add(x,y)}")
print(f"Their difference is {x} - {y} = {diff(x,y)}")
print(sort(x,y,add(x,y),diff(x,y)))

#%% increment
def increment(y):
    '''Argument passed is incremented it.'''

    return (lambda y:y+1)(y)

a = int(input("Enter a number to be incremented: "))
print(f"This is your number before increment: {a}")
b = increment(a)
print(f"This is your number after increment: {b}")

#%% printing lambda function directly
twice = lambda x:x*2
print(twice(9))

print((lambda x:x*2)(90))

#%% passing lambda function as an argument to another function
multiply = lambda x,y:x*y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def cube(a):
    '''Arguments passed through it are cubed.'''

    return a**3

print(f"The multiplication value of {num1} x {num2} = {multiply(num1, num2)}")
print("The cubed value is: ",cube(multiply(num1, num2)))