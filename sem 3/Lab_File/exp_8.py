# WAP to find the index of an item in a specified list.

input_list = input("Enter items of list separated by spaces: ").split(" ")
to_find = input("Enter item to be found: ")

if to_find in input_list:
    print(f"Index of {to_find} is {input_list.index(to_find)}")

else:
    print("Item not in list")
