# base class
class Base:
    
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def publicBase(self):
        print("Base method, public member:",self.var1)

    def _protectedBase(self):
        print("Base method, protected member:",self._var2)

    def __privateBase(self):
        print("Base method, private member:",self.__var3)

    def accessPrivate(self): 
        self.__privateBase()


# derived class
class Derived(Base):

    def __init__(self, var1, var2, var3):
        Base.__init__(self, var1, var2, var3)

    def publicDerived(self):
        self.publicBase()

    def _protectedDerived(self):
        self._protectedBase()

    def privateDerived(self):
        self.__privateBase()
    
    def fun(self):
        print("Public member:",self.var1)
        print("Protected member:",self._var2)
        print("Private member:",self.__var3)

obj = Derived(10,20,30)

print(obj.var1)

print(obj._var2)

# print(obj.__var3) # error

obj.publicBase()

obj._protectedBase()

# obj.__privateBase() # error

obj._protectedDerived()

# obj.privateDerived() # error

# obj.fun() # error

# %%
class Base:

    def __init__(self, var1, var2, var3):

        self.pub = var1
        self._pro = var2
        self.__pri = var3

    def displayPublic(self):
        print("Public Data Member:", self.pub)                

    def _displayProtected(self):
        print("Protected Data Member:", self._pro)

    def __displayPrivate(self):
        print("Private Data Member:", self.__pri)

    def accessPrivate(self): 
        self.__displayPrivateMembers()

class Derived(Base):
    
    def __init__(self, var1, var2, var3):
        Base.__init__(self, var1, var2, var3)

    def accessProtected(self):
        self._displayProtected()

    def fun(self):
        print(self.pub)
        print(self._pro)
        print(self.__pri)

obj = Derived(10,20,30)

print(obj.pub)

print(obj._pro)

# print(obj.__pri)

obj.displayPublic()

obj._displayProtected()

# obj.__displayPrivate()

obj.accessProtected()

# obj.accessPrivate()

# obj.fun()
