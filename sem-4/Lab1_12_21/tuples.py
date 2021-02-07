print("\n--- Create a tuple ---")
tuple_one = (1, 2, 3)
print(tuple_one)
print(type(tuple_one))

print("\n--- Create tuple with different data types ---")
tuple_two = (1, 0.56, 'a string', [1, 2, 3])
print(tuple_two)

print("\n--- Create tuple with numbers and print ine item ---")
tuple_three = (1, 2, 3, 4)
print(tuple_three[1])

print("\n--- Add item to tuple ---")
tuple_four = tuple_one + tuple_three
print(tuple_four)

print("\n--- Convert tuple to a string ---")
tuple_five = ('this', 'is', 'a', 'string', 'converted', 'from', 'a', 'tuple')

converted_tuple = " ".join(tuple_five)
print(converted_tuple)
print(type(converted_tuple))
