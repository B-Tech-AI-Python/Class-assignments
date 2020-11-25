# %%
# WAP to understand the different basic data types and expressions
print("Integer")
int_num = 1
print(int_num, "is", type(int_num))

# %%
print("Float")
float_num = 1.0
print(float_num, "is", type(float_num))

# %%
print("Complex Number")
complex_num = 1 + 8j
print(complex_num, "is", type(complex_num))

# %%
print("Strings")
string1 = 'This is a string with (\') an escape character'
string2 = "First line.\nA newline.\nAnother newline."
string3 = "A string with a \tTAB"
string4 = """A
multiline
string"""
string5 = f"This is {int_num} formatted string."
string6 = r"Raw\\String"

print("\nString 1")
print(string1)

print("\nString 2")
print(string2)

print("\nString 3")
print(string3)


print("\nString 4")
print(string4)

print("\nString 5")
print(string5)

print("\nString 6")
print(string6)

# %%
print("Booleans")
condition = True

if condition:
    print('Condition is True')
