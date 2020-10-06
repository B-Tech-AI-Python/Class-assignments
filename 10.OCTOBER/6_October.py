class Base1:
    def __init__(self):
        print('Base1')
        super(Base1, self).__init__()

class Base2:
    def __init__(self):
        print('Base2')
        super(Base2, self).__init__()

class Base3:
    def __init__(self):
        print('Base3')

class Derived(Base1, Base2, Base3):
    def __init__(self):
        super(Derived, self).__init__()
        print('Derived')

obj = Derived()
