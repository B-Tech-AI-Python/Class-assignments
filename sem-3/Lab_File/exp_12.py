"""Design a Python program as described below:

a. Create a class called Palindrome.

b. In your Palindrome class, create a method called reverse()
which takes a string argument.Your method should return the
reverse of the argument as a string.

c. Create a second method in Palindrome called isPalindrome()
which takes a string argument. This method should return True
if the argument is a palindrome and False otherwise.

d. Write some code to test your new Palindrome class and print
out results of your testing to the user. Give some consideration
to what sort of strings you might want to use for your testing.

"""


class Palindrome():
    def __init__(self, input_string):
        self.string = input_string

    def reverse(self):
        self.reverse_string = self.string[::-1]
        return self.reverse_string

    def isPalindrome(self):
        if self.reverse_string == self.string:
            return True
        return False
    
    def __str__(self):
        return self.string


not_a_palindrome = "I am not a palindrome"
a_palindrome = "madam"

obj1 = Palindrome(not_a_palindrome)
print(obj1)
print(obj1.reverse())
print(obj1.isPalindrome())

print()
obj2 = Palindrome(a_palindrome)
print(obj2)
print(obj2.reverse())
print(obj2.isPalindrome())
