# print in different lines
print("Good")
print("Morning")

# %% print in same line
print()
print("Good", end=" ")
print("Morning")

# %% str and int cannot be concantenated
print()
str = "hello" + '007'
print(str)

# %% id
print()
str1 = "elephants are amazing"
str2 = "elephants are amazing"
str3 = "Hello"

print(id(str1), id(str2), id(str3))

# %% methods
print()
str1 = "elephants are amazing"

print(str1.capitalize())
print('----------------------------------------------------------------------')
print(str1.center(10, '*'))
print('----------------------------------------------------------------------')
print(str1.zfill(10))
print('----------------------------------------------------------------------')
print(str1.lower())
print('----------------------------------------------------------------------')
print(str1.upper())
print('----------------------------------------------------------------------')
print(str1.lstrip())
print('----------------------------------------------------------------------')
print(str1.rstrip())
print('----------------------------------------------------------------------')
print(str1.strip())
print('----------------------------------------------------------------------')
print(min(str1))
print('----------------------------------------------------------------------')
print(max(str1))
print('----------------------------------------------------------------------')
print(str1.replace('amaz', 'confus'))
print('----------------------------------------------------------------------')
print(str1.title())
print('----------------------------------------------------------------------')
print(str1.swapcase())
print('----------------------------------------------------------------------')
print(str1.split(','))
print('----------------------------------------------------------------------')
print('/'.join(str1))
print('----------------------------------------------------------------------')
print(str1.isidentifier())
print('----------------------------------------------------------------------')
print(list(enumerate(str1)))

# %% slicing
print()
str1 = "elephants are amazing"

print(str1[0:])
print('----------------------------------------------------------------------')
print(str1[:10])
print('----------------------------------------------------------------------')
print(str1[0::2])
print('----------------------------------------------------------------------')
print(str1[-10:-3:1])
print('----------------------------------------------------------------------')
print(str1[::-1])

# %% ASCII
print()
print("The alphabet and it's ASCII value are:\n")
for i in range(ord('A'), ord('Z')+1):
    print(chr(i), ord(chr(i)), '&', chr(i).lower(), ord(chr(i).lower()))

# %%
print()


def table(num):
    print(f"\nThe table for {num} is:\n")

    for i in range(1, 10):
        print(f" {i}  x {num} = {i*num}")
    for i in range(10, 11):
        print(f" {i} x {num} = {i*num}")
    print("-----------------")


table(5)
table(10)
table(20)
table(25)
table(100)
