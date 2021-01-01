print("\n--- Create a set ---")
set_one = {1, 3, 5, 7}
print(set_one)
print(type(set_one))

print("\n--- Add member(s) in a set ---")
set_two = {2, 3, 5, 7}
print(set_two)

print("Adding 11 to current set:", end=" ")
set_two.add(11)

print(set_two)
print(type(set_two))

print("\n--- Remove item(s) from a set ---")
to_remove = int(input("Enter number to remove from set: "))
set_two.discard(to_remove)
print(set_two)

print("\n--- Remove item if it is present in the set ---")
to_remove = int(input("Enter number to remove from set: "))

try:
    set_two.remove(to_remove)
    print(set_two)
except:
    print("Value not present in set!")
    print("This is your set:", set_two)
