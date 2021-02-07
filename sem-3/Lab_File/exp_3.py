# WAP to find the simple interest for a given value P, T and R.
# The program must take the input from the user.


def simple_interest(p, r, t):
    print("\nYour principal amount is:", p)
    print("Your rate of interest is:", r)
    print("Your time (in years) is:", t)

    return (p*r*t) / 100


principal_amt = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))


print("Your simple interest is:", simple_interest(principal_amt, rate, time))
