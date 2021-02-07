# WAP to get the frequency of the elements in a list.

input_list = input("Enter items of list separated by spaces: ").split(" ")

number_of_items = {}

for item in input_list:
    if item in number_of_items:
        number_of_items[item] += 1
    else:
        number_of_items[item] = 1

for key, value in number_of_items.items():
    print(f"{key}: {value}")
