"""A bookshop details contains the Title of the book and Number
of copies of each title. As books are added to the shop, the number
of copies to each should increase and as books are sold, the number
of copies in each should decrease.

Implement this scenario using dictionary data type in Python.

"""

import pandas as pd

books = {"Hunger Games": 3,
         "The Book Thief": 2,
         "All The Bright Places": 7,
         "Turtles All The Way Down": 4}


def add_book(book_title, copies):
    if book_title.title() in books:
        books[book_title] += copies

    else:
        books[book_title] = copies

    print("Book added!")


def sell_book(book_title, copies):
    if book_title.title() in books:
        books[book_title] -= copies
        print("Book sold!")

    else:
        print("Error! Book not in system.")


def display_books():
    print(pd.DataFrame.from_dict(books, orient="index", columns=["Number of Copies"]))


while True:
    print("\n-----CHOICES-----")
    print("1. Add Book")
    print("2. Sell Book")
    print("3. Display Books")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title you want to add: ")
        number = int(input("Enter number of copies of the book: "))

        add_book(title, number)

    elif choice == 2:
        title = input("Enter book title sold: ")
        number = int(input("Enter number of copies sold: "))

        sell_book(title, number)

    elif choice == 3:
        display_books()

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Wrong input! Try again!")
