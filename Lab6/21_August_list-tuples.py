# 4th element and 4th last element
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f"The 4th element is {my_tuple[3]}")
print(f"The 4th last element is {my_tuple[-3]}")

# %% repeated items

my_tuple2 = (1,1,1,1,2,2,2,3,4,5,6,6,6,7,8,8)

def repeat(my_tuple):
    repeated_items = []

    for i in my_tuple:
        if my_tuple.count(i) > 1:
            if i not in repeated_items:
                repeated_items.append(i)

    return repeated_items


print(repeat(my_tuple2))


# %% finding item
import random

random_list = list()

for i in range(11):
    n = random.randint(0,11)
    random_list.append(n)

my_tuple3 = tuple(random_list)

num = int(input("Enter number you want found: "))

if num in my_tuple3:
    print(f"{num} found in the tuple!")
    print(f"The current tuple is: {my_tuple3}")

else:
    print(f"{num} not found in the tuple!")
    print(f"The current tuple is: {my_tuple3}")
    
# %% removing item
my_tuple4 = tuple(int(item) for item in input("Enter the elements of tuple: ").split())

num = int(input("Enter number you want to remove: "))

x = list()

if num in my_tuple4:
    print(f"{num} found and removed from the tuple!")
    
    for i in my_tuple4:
        if i != num:
            x.append(i)
    
    new_tuple = tuple(x)
    print(f"The current tuple is: {new_tuple}")

else:
    print(f"{num} not found in the tuple!")
    print(f"The current tuple is: {my_tuple4}")

# %% Replacing first item
my_tuple5 = tuple(int(item) for item in input("Enter the elements of tuple: ").split())

num = int(input("Enter number you want in place of first element: "))

x = [num]

for num in range(2,len(my_tuple5)+1):
    x.append(num)


new_tuple = tuple(x)    
print(f"The current tuple is: {new_tuple}")

# %% repeatd items
my_tuple6 = tuple(int(item) for item in input("Enter the elements of tuple: ").split())

def repeat2(my_tuple):
    repeated_items = []

    for i in my_tuple6:
        if my_tuple.count(i) >= 1:
            if i not in repeated_items:
                repeated_items.append(i)


    return repeated_items


print(tuple(repeat2(my_tuple6)))

# %% matching lists

list1 = list(int(item) for item in input("Enter the elements of first list: ").split())

list2 = list(int(item) for item in input("Enter the elements of second list: ").split())

matching_elements = list()

for item in list1:
    if item in list2:
        matching_elements.append(item)

if len(matching_elements) > 0:
    print("\nTrue!")
    print(f"The matching elemnts are {matching_elements}")

else:
    print("No matching elements!")

# %%
list_of_strings = list(item for item in input("Enter the elements of list: ").split())

def repeat3(list_of_strings):
    repeated_items = []

    for i in list_of_strings:
        if list_of_strings.count(i) > 1:
            if i not in repeated_items:
                repeated_items.append(i)

    return repeated_items


print(repeat3(list_of_strings))

# %%
string_list = list(item for item in input("Enter the elements of list: ").split())

n = int(input("Enter limit: "))

print("\nThe longer elements: ")
for i in string_list:
    if len(i) > n:
        print(i)
