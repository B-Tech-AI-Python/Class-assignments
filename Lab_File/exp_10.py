# WAP to convert a list of tuples into a dictionary

a_list = [("Name1", 1), ("Name2", 2), ("Name3", 3), ("Name4", 4), ("Name5", 5)]
a_dict = {}

for item in a_list:
    if item[0] not in a_dict:
        a_dict[item[0]] = item[1]
    else:
        a_dict[item[0]] += item[1]

print(a_dict)
