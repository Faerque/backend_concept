from models.book import Book
from models.library import Library
from views.library_view import LibraryView

class LibraryController:
    def __init__(self, library, view):
        self.library = library
        self.view = view

    def add_book(self, title, author):
        book = Book(title, author)
        self.library.add_book(book)
        self.view.display_message(f"Book '{title}' added successfully.")

    def remove_book(self, title):
        if self.library.remove_book(title):
            self.view.display_message(f"Book '{title}' removed successfully.")
        else:
            self.view.display_message(f"Book '{title}' not found in the library.")

    def display_books(self):
        books = self.library.get_books()
        self.view.display_books(books)
