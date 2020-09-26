# 1
cse13 = list()

students = int(input("Enter number of students in class: "))
 
for i in range(1, students+1):

    while True:
        try:
            name = input(f"Enter name of student {i}: ")
            grade = int(input(f"Enter overall grade of student {i}: "))

            # check if name in letters and grade is integer
            if name.isalpha() and isinstance(grade, int):
                temp = [name, grade]
                cse13.append(temp)
                break

            else:
                raise ValueError

        except ValueError:
            print("INVALID! Try again!")

# the nested list
print("\n----------------------------------")
print("The nested list is:")
print(cse13)
print("-----------------------------------")

# first element sort
def firstElement(element):
    return element[0]

# second element sort
def secondElement(element):
    return element[1]

# sort according to marks
cse13.sort(key = secondElement)

# second least marks
if cse13[0][1] == cse13[1][1]:
    if len(cse13) > 2:
        second_least_marks = cse13[2][1]
        second_least = cse13[2]

        # count
        count = sum(x.count(second_least_marks) for x in cse13)

    else:
        pass

else:
    if all(number == cse13[0] for number in cse13):
        pass
    else:
        second_least_marks = cse13[1][1]
        second_least = cse13[1]

        # count
        count = sum(x.count(second_least_marks) for x in cse13)

# checking how many students have second least marks
try:
    if count == 1:
        print("\nThe student with the second least marks:")
        for item in second_least:
            print("Name         Grade")
            print(item, end="           ")

    elif count > 1:
        temp2 = list()

        for item in cse13:
            if item[1] == second_least_marks:
                temp2.append(item)

        temp2.sort(key = firstElement)
        print("\nThe students with the second least marks:")
        for item in temp2:
            print("Name          Grade")
            print(item[0], "            ", item[1])

    else:
        print("\nNo second least marks!")

except NameError:
    print("\nNo second least marks!")

# %% 2
my_list = list()

print("\n----- input list -----")
input_items = input("Enter list of intgers for list (separate them with spaces): ").split(" ")

for item in input_items:

    item = int(item)
    my_list.append(item)

print(my_list)

print("\n----- insert item -----")
insert_item = int(input("Enter integer to be inserted: "))
position = int(input("Enter position to be inserted at: "))
my_list.insert(position-1,insert_item)

print(my_list)

print("\n----- remove item -----")
remove_value = int(input("Enter integer to be removed: "))
my_list.remove(remove_value)

print(my_list)

print("\n----- append item -----")
append_item = int(input("Enter integer to be appended: "))
my_list.append(append_item)

print(my_list)

print("\n----- sort list -----")
my_list.sort()

print(my_list)

print("\n----- pop item -----")
my_list.pop()

print(my_list)

print("\n----- reverse list -----")
reverse_list = my_list[::-1]

print(reverse_list)
