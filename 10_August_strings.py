import pandas as pd

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
print("Multiplication tables\n")


def table(num):

    lis = []
    for i in range(1, 11):
        lis.append(f"{num} x {i}")

    return lis


def values(num):

    lis = []
    for i in range(1, 11):
        lis.append(i*num)

    return lis


tableOf5 = {'Table': table(5), 'Value': values(5)}
tableOf10 = {'Table': table(10), 'Value': values(10)}
tableOf20 = {'Table': table(20), 'Value': values(20)}
tableOf25 = {'Table': table(25), 'Value': values(25)}
tableOf50 = {'Table': table(50), 'Value': values(50)}
tableOf100 = {'Table': table(100), 'Value': values(100)}


df5 = pd.DataFrame(tableOf5, columns=['Table', 'Value'])
df10 = pd.DataFrame(tableOf10, columns=['Table', 'Value'])
df20 = pd.DataFrame(tableOf20, columns=['Table', 'Value'])
df25 = pd.DataFrame(tableOf25, columns=['Table', 'Value'])
df50 = pd.DataFrame(tableOf50, columns=['Table', 'Value'])
df100 = pd.DataFrame(tableOf100, columns=['Table', 'Value'])


print(df5)
print()
print(df10)
print()
print(df20)
print()
print(df25)
print()
print(df50)
print()
print(df100)
print()
