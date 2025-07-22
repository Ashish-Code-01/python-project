class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def print_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

    def get_no_of_books(self):
        return self.no_of_books

# Demonstration
library = Library()
library.print_books()  # Should show no books

library.add_book("The Great Gatsby")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")

library.print_books()  # Should print all books
print(f"Number of books: {library.get_no_of_books()}")

# Add another book
library.add_book("Pride and Prejudice")
print(f"Number of books after adding one more: {library.get_no_of_books()}")

# Note: If you stop and rerun this program, the library will be empty again.