class LibraryView:
    @staticmethod
    def display_books(books):
        if not books:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in books:
                print(f" - {book}")

    @staticmethod
    def display_message(message):
        print(message)
