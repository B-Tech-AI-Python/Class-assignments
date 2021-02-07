print("\n--- Add a key ---")
dictionary_one = {'zero': 0, 'one': 1, 'two': 2}
print("Original dictionary:", dictionary_one)

dictionary_one.update({'three': 3})
print("New dictionary:", dictionary_one)

print("\n--- Concatenate dictionaries to create a new one ---")
dictionary_two = {'four': 4, 'five': 5, 'six': 6}
dictionary_one.update(dictionary_two)
print(dictionary_one)

print("\n--- Check if a key is present ---")
check_key = input("Enter key to be checked: ")

if check_key in dictionary_one:
    print("Key exists in dictionary")
else:
    print("Key doesn't exist in dictionary")
