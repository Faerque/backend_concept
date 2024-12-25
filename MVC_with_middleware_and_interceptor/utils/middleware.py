class Middleware:
    @staticmethod
    def validate_book_input(title, author):
        if not title or len(title.strip()) == 0:
            raise ValueError("Book title cannot be empty.")
        if not author or len(author.strip()) == 0:
            raise ValueError("Author name cannot be empty.")
