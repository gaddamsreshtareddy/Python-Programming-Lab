# Library Management System

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        print("\n----- AVAILABLE BOOKS -----")
        for book in self.books:
            print(book)


library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.display_books()