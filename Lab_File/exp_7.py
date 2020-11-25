# WAP to convert a list of characters into a string.

def into_string(a_list):
    return "".join(a_list)


input_list = input("Enter characters separated by spaces: ").split(" ")

print(into_string(input_list))
