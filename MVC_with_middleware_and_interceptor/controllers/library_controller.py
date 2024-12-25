from models.book import Book
from models.library import Library
from views.library_view import LibraryView
from utils.middleware import Middleware
from utils.interceptor import Interceptor

class LibraryController:
    def __init__(self, library, view):
        self.library = library
        self.view = view

    def add_book(self, title, author):
        try:
            Middleware.validate_book_input(title, author)  # Middleware validation
            book = Book(title, author)
            self.library.add_book(book)
            Interceptor.log_action("Add Book", {"title": title, "author": author}, success=True)  # Interceptor logging
            self.view.display_message(f"Book '{title}' added successfully.")
        except ValueError as e:
            Interceptor.log_action("Add Book", {"title": title, "author": author}, success=False)
            self.view.display_message(str(e))

    def remove_book(self, title):
        try:
            Middleware.validate_book_input(title, "Dummy Author")  # Validate title only
            if self.library.remove_book(title):
                Interceptor.log_action("Remove Book", {"title": title}, success=True)
                self.view.display_message(f"Book '{title}' removed successfully.")
            else:
                Interceptor.log_action("Remove Book", {"title": title}, success=False)
                self.view.display_message(f"Book '{title}' not found in the library.")
        except ValueError as e:
            Interceptor.log_action("Remove Book", {"title": title}, success=False)
            self.view.display_message(str(e))

    def display_books(self):
        books = self.library.get_books()
        Interceptor.log_action("Display Books", {"count": len(books)}, success=True)
        self.view.display_books(books)
