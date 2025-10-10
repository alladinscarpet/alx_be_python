"""
you’ll define a base class Book and two derived classes,
EBook and PrintBook, showcasing inheritance.
Additionally, implement a Library class
demonstrating composition by managing a collection of books.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Defines how an object is represented as a string.
    def __str__(self):
        return f"Book: {self.title} by {self.author}"




class EBook(Book):
    def __init__(self, title, author, file_size):

        # Initialize attributes from the parent class
        super().__init__(title, author)
        self.file_size = file_size

    # Defines how an object is represented as a string.
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):

        # Initialize attributes from the parent class
        super().__init__(title, author)
        self.page_count = page_count

    # Defines how an object is represented as a string.
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = [] # list of Book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        available_found = False

        for book in self.books:
            print(book)
            available_found = True

        if not available_found:
            print("No books available")



