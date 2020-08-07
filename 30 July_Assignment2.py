#Greatest common divisor
def gcd(x,y):
    
    for num in range(1,max(x,y)+1):
        if x%num == 0 and y%num == 0:
            gcd = num
    return gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The greatest common divisor of {num1} and {num2} is {gcd(num1,num2)}")

#%% exp(x,y)
def exp(x,y):
    pass

#%%  fibonacci series 
def fibonacci(x):
    pass

#%% to find the number of times a recursive function is called

#%% concatenate two strings using recursion
def concatenate():
    pass

#%%  menu driven program using functions to perform calculator operations
def calc(choice,num1,num2):
    if choice == 1:
        return num1+num2
    elif choice ==2:
        return num1-num2
    elif choice == 3:
        return num1*num2
    elif choice == 4:
        return num1/num2
    else:
        pass

print("-----MENU-----")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        choice = float(input("What operation would you like to perform? "))
        if type(choice) == float and type(num1) == float and type(num2) == float:
            if choice in range(1,5):
                print(calc(choice,num1,num2))
                break
            else:
                print("INVALID!\nEnter a choice between 1-4!")
        else:
            raise ValueError

    except ValueError:
        print("INVALID INPUT!")

    finally:
        print("Operation successfully performed!")

#%% lmbda function to find smallest number
small = lambda x,y: print("\nThey are equal!") if x==y else print("\nThe smallest number is", min(x,y))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
small(num1,num2)
#%% to compute lambda(n) for all positive values of n
func = lambda x : 1 if x < 1 else func(x/2) + 1

for num in range(1000):
    print(func(num),end=" ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    