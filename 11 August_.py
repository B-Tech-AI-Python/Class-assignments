str1 = input("Enter your string: ")

str2 = 'hello'

if str2 in str1:
    print("Present!")
else:
    print("Not present!")

for i in str2:
    print(i)

i = 0

while i < len(str2):
    letter = str2[i]
    print(letter)
    i += 1

# %%
str2 = 'hello'
vowels = ['a', 'e', 'i', 'o', 'u']

print(str2)

for i in str2:
    if i not in vowels:
        print(i, end="")

# %%
username = input("Enter username: ")
password = input("Enter password: ")

print(username)
for i in range(len(password)):
    print('*', end="")
