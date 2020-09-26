class Demo:
    
    class_var = 0
    
    def __init__(self, var):
        Demo.class_var += 1
        self.var = var
        
        print("var:",var)
        print("self.var:",self.var)
        print("Demo.class_var:",Demo.class_var)
    
    def __del__(self):
        Demo.class_var -= 1
        print(f"Object with value {self.var} is going out of scope")

print()
obj1 = Demo(10)
print()
obj2 = Demo(20)
print()
obj3 = Demo(30)

print()
del obj1
print()
del obj2
print()
del obj3
