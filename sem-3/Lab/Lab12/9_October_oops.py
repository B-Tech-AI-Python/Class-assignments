class M:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, obj):
        return self.a + obj.a
    
    def __sub__(self, obj):
        return self.a - obj.a
    
    def __gt__(self, obj):
        return (self.a > obj.a)

num1 = M(1)
num2 = M(2)

print("\nAddition of numbers")
print(num1 + num2)

print("\nSubtraction of numbers")
print(num1 - num2)
print(num2 - num1)

print("\nGreater than of numbers")
print(num1 > num2)

st1 = M("Good")
st2 = M("Morning")

print("\nConcatenation of strings")
print(st1 + st2)
print(st2 + st1)

print("\nGreater than of numbers")
print(st1 > st2)
print(st2 > st1)

