class Base1:
    def __init__(self):
        print('Base1')

class Base2:
    def __init__(self):
        print('Base2')
        super(Base2, self).__init__()


class Derived(Base2,Base1):
    def __init__(self):
        super(Derived, self).__init__()
        print('Derived')

obj = Derived()
