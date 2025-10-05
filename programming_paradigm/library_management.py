class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Was not checked out

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
        def __init__(self):
            self._books = []  # Private list of Book instances

        def add_book(self, book):
            """Add a Book object to the library."""
            self._books.append(book)

        def check_out_book(self, title):
            """Check out a book by title."""
            for book in self._books:
                if book.title == title:
                    if book.check_out():
                        return f"'{title}' has been checked out."
                    else:
                        return f"'{title}' is already checked out."
            return f"'{title}' not found in library."

        def return_book(self, title):
            """Return a book by title."""
            for book in self._books:
                if book.title == title:
                    if book.return_book():
                        return f"'{title}' has been returned."
                    else:
                        return f"'{title}' was not checked out."
            return f"'{title}' not found in library."

        def list_available_books(self):
            """Print all available books."""
            available_books = [book for book in self._books if book.is_available()]
            if not available_books:
                print("No books available.")
            else:
                for book in available_books:
                    print(f"{book.title} by {book.author}")
