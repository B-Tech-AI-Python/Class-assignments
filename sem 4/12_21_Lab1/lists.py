user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sum of all items
print(f"\nSum of all items in the list: {sum(user_list)}")

# largest number
print(f"\nLargest number in the list: {max(user_list)}")

# smallest number
print(f"\nSmallest number in the list: {min(user_list)}")

# multiplication of all the numbers
total = 1
for number in user_list:
    total *= number

print(f"\nMultplied result of all numbers in the list: {total}")
