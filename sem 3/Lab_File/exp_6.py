"""WAP to

Create two new files f1 and f2.

Read and display the contents, count the number of lines and find the word whose
count is more in f1 and f2 respectively.

Create and display the file f3 which is a combination of f1 and f2.

"""
# file 1
with open("Lab_File/file1", "w") as file:
    file.write("Line1\nLine2\nLine3\nLine4\nPotato is a long word.\n")

with open("Lab_File/file1", "r") as file:
    print("\nFile 1 contents")
    print(file.read())

    file.seek(0)

    longest_word = ''
    content = []

    for word in file.readlines():
        content.append(word.split())

    for lines in content:
        for word in lines:
            if len(word) > len(longest_word):
                longest_word = word

    print(f"\nThe longest word is: {longest_word}")

    file.seek(0)

    print(f"\nNumber of lines in file 1: {len(file.readlines())}")

print()

# file 2
with open("Lab_File/file2", "w") as file:
    file.write("Line1\nLine2\nLine3\nWatermelon is a long word.\n")

with open("Lab_File/file2", "r") as file:
    print("\nFile 2 contents")
    print(file.read())

    file.seek(0)

    longest_word = ''
    content = []

    for word in file.readlines():
        content.append(word.split())

    for lines in content:
        for word in lines:
            if len(word) > len(longest_word):
                longest_word = word

    print(f"\nThe longest word is: {longest_word}")

    file.seek(0)

    print(f"\nNumber of lines in file 2: {len(file.readlines())}")


print()
# comparing
with open("Lab_File/file1", "r") as f1, open("Lab_File/file2", "r") as f2, open("Lab_File/file3", "w") as f3:
    for line in f1.readlines():
        f3.write(line)

    for line in f2.readlines():
        f3.write(line)

with open("Lab_File/file3", "r") as file:
    print("\nFile 3 contents")
    print(file.read())
