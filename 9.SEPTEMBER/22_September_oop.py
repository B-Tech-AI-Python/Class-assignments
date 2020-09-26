# public and private
class Demo1:
    
    def __init__(self, var1, var2):
        self.var1 = var1
        self.__var2 = var2
    
    def publicMethod(self):
        print("Public method")
        print("Class method, public member:",self.var1)
        print("Class method, private member:",self.__var2)
    
    def __privateMethod(self):
        print("Private method")
        print("Class method, public member:",self.var1)
        print("Class method, private member:",self.__var2)

obj1 = Demo1(1,2)

obj1.publicMethod()

print()
# obj1.privateMethod()                                      error
# obj1.__privateMethod()                                    error
obj1._Demo1__privateMethod() 

print()

print("Main module, public member:",obj1.var1)
# print("Main module, private member:",obj1.__var2)          error
print("Main module, private member:",obj1._Demo1__var2)

# %% calling function from outside
def outFunc(var):
    return var**2

class Demo2:
    
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def method1(self):
        print("Square of var1:",outFunc(self.var1))
        print("Square of var2:",outFunc(self.var2))
    
    def squaring(self):
        self.var1 = outFunc(self.var1)
        self.var2 = outFunc(self.var2)

obj2 = Demo2(10, 20)

print("\nVariables")
print(obj2.var1)
print(obj2.var2)

print("\nMethod1")
obj2.method1()

print("\nVariables")
print(obj2.var1)
print(obj2.var2)

print("\nSquaring")
obj2.squaring()

print("\nVariables")
print(obj2.var1)
print(obj2.var2)

#%%
