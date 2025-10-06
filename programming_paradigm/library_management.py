"""
Solidify understanding of basic OOP concepts in Python
by implementing a system that tracks books in a library,
focusing on classes, object instantiation, and method invocation.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out # opposite of is checked out



class Library:
    def __init__(self):
        self._books = [] # list of Book objects

    def add_book(self, book):
        self._books.append(book)


    def check_out_book(self, title):
        for book in self._books:
    # Python trusts that everything in the list supports those attributes and methods.
    # So as long as you’re adding actual Book objects, it’ll work perfectly.
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return # stops searching & exit func as soon as it finds the right book.

        print("Book not available")


    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned")
                return

        print("Book already returned")

    def list_available_books(self):
        available_found = False

        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True

        if not available_found:
            print("No books available")


# always create Book objects (outside Library)
# as library class only receive them and store them
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

# Create Library object
library = Library()

# Add books to the library
# This is a general OOP design principle called composition.
# Composition means a class (like Library)
# “has” other objects (like Book),
# but doesn’t necessarily create them.
library.add_book(book1)
library.add_book(book2)

# Initial list of available books
print("Available books after setup:")
library.list_available_books()
print()

# Simulate checking out a book
library.check_out_book("1984")
print("\nAvailable books after checking out '1984':")
library.list_available_books()
print()


# Simulate returning a book
library.return_book("1984")
print("\nAvailable books after returning '1984':")
library.list_available_books()


