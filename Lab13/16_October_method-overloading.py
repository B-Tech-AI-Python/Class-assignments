# method overloading
from multipledispatch import dispatch

@dispatch(int,int)
def product(x,y):
    result = x*y
    print(f"int,int: {result}")

@dispatch(int,int,int)
def product(x,y,z):
    result = x*y*z
    print(f"int,int,int: {result}")

@dispatch(float,float,float)
def product(x,y,z):
    result = x*y*z
    print(f"float,float,float: {result}")

product(1,2)
product(1,2,3)
product(1.1,2.2,3.3)

