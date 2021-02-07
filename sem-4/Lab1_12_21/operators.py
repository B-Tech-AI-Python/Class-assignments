# \\OPERATORS\\
# arithmetic
# comparison
# assignment
# logical
# membership

vowels = ['a', 'e', 'i', 'o', 'u']

user_name = input("\nEnter your name: ")
print("\nHello" + " " + user_name + "!")

count = 0

for letter in vowels:
    if letter in user_name.lower():
        count += 1

if count > 0:
    print(f"\nYou have {count} vowels in your name.")

else:
    print("\nYou have no vowels in your name.")

if len(user_name) >= 6:
    print("\nYou have a long name!")

