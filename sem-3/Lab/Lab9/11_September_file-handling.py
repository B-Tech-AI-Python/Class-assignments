# writing on file 1
f1 = open("file1.txt", "w")

f1.write("TThis is my line 1.\nThis is my line 2.\nThis is my line 3.\nThis is my line 4. ")

f1.close()
f1 = open("file1.txt", "r")

print("The data in file 1:\n")
print(f1.read())

f1.close()

# %% appending
f1 = open("file1.txt", "a")

input_string = input("Enter data you want to append to file 1: ")
f1.write(input_string)

f1.close()

with open("file1.txt", "r") as f1:
    print("This is the data in file 1:\n")
    print(f1.read())

# %% longest words
with open("file1.txt", "r") as f1:
    words = f1.read().split()
    print(words)
    max_len = len(max(words, key=len))
    print(max_len)
    print()
    longest_words = [word for word in words if len(word) == max_len]

print("The longest words:\n")
for i in longest_words:
    print(i)

# %% copy file data
with open("file1.txt", "r") as f1:
    with open("file2.txt", "w") as f2:
        for line in f1:
            f2.write(line)

with open("file2.txt", "r") as f2:
    print("This is the data in file 2:\n")
    print(f2.read())

# %% merging file 1 and file 2 to file 3
with open("file1.txt", "r") as f1:
    file1 = f1.readlines()

with open("file2.txt", "r") as f2:
     file2 = f2.readlines()

with open("file3.txt", "w") as f3:
    
    if len(file1) == len(file2):
        for i in range(len(file1)):
            f3.write(file1[i] + file2[i] + '\n')

    elif len(file1) > len(file2):
        for i in range(len(file2)):
            f3.write(file1[i] + file2[i] + '\n')
        for i in range(len(file2),len(file1)):
            f3.write(file1[i] + '\n')
            
    elif len(file1) < len(file2):
        for i in range(len(file1)):
            f3.write(file1[i] + file2[i] + '\n')
        for i in range(len(file1),len(file2)):
            f3.write(file2[i] + '\n')

with open("file3.txt", "r") as f3:
    print("This is the data in file 3:\n")
    print(f3.read())

# %% delete specific line
with open("file1.txt", "r") as f1:
    file1 = f1.readlines()

line_num = int(input("Which line do you want to delete: "))

file1.pop(line_num-1)

with open("file1.txt", "w") as f1:
    for line in file1:
        f1.write(line)

with open("file1.txt", "r") as f1:
    print("\nThis is the data in file 1:\n")
    print(f1.read())

