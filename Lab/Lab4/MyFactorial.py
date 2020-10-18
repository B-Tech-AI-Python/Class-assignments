# Ishani Kathuria A023119819004

import module

while True:
    try:
        num = int(input("Enter number to find factorial: "))
        if type(num) == int:
            break
        else:
            raise ValueError
    except ValueError:
        print("INVALID INPUT! TRY AGAIN\n")

print("The factorial is:",module.fact(num))
