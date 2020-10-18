# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


n = int(input("Enter a number to caculate it's factorial: "))
print("Factorial is:", factorial(n))

# %%
# Max marks


def max_marks():
    inpt = []
    marks = [0]
    inpt = input("Enter the marks for 5 students: ").strip().split()
    for i in inpt:
        i = int(i)
        marks.append(i)
    print("The maximum marks scored are", max(marks), "by student", marks.index(max(marks)))


max_marks()

# %%


def myfunc(st):
    str = ''
    for index, l in enumerate(st):
        if index % 2 == 0:
            str += l.upper()
        else:
            str += l.lower()
    return str


print(myfunc(input("Enter string: ")))

# %%


def words():
    word1, word2 = input("Enter 2 words: ").strip().split()
    if word1[0].upper() == word2[0].upper():
        return True
    else:
        return False


result = words()
print(result)
