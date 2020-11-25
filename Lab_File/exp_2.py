# WAP to read two integers and find the sum, diff, mult and div.

def sum(num_1, num_2):
    return num_1+num_2


def difference(num_1, num_2):
    return num_1-num_2


def multiply(num_1, num_2):
    return num_1*num_2


def divide(num_1, num_2):
    return num_1/num_2


first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

while True:
    print("\n1. Sum")
    print("2. Difference")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("What do you want to do? (1-5): "))

    if choice == 1:
        print(f"{first_num} + {second_num} = {sum(first_num, second_num)}")

    elif choice == 2:
        print(f"{first_num} - {second_num} = {difference(first_num, second_num)}")

    elif choice == 3:
        print(f"{first_num} * {second_num} = {multiply(first_num, second_num)}")

    elif choice == 4:
        print(f"{first_num} / {second_num} = {divide(first_num, second_num)}")

    else:
        print("Goodbye!")
        break
