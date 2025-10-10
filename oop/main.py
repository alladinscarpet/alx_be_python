'''
To test your Book class from book_class.py,
use the following main.py script,
which demonstrates creating a Book instance
and utilizing the implemented magic methods:
'''

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", "1949")

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()