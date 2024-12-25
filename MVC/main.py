from models.library import Library
from views.library_view import LibraryView
from controllers.library_controller import LibraryController


def display_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. View All Books")
    print("4. Exit")


if __name__ == "__main__":
    print("Initializing the Library Management System...\n")

    # Initialize Model, View, and Controller
    print("Model: Initializing the library to store data.")
    library = Library()

    print("View: Setting up the user interface for interaction.")
    view = LibraryView()

    print("Controller: Connecting the model and the view.")
    controller = LibraryController(library, view)

    print("\nSystem ready! You can now interact with the Library Management System.\n")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Add a book
            title = input("Enter the title of the book: ").strip()
            author = input("Enter the author of the book: ").strip()
            print("\nController: Adding a book to the library through the model.")
            controller.add_book(title, author)

        elif choice == "2":
            # Remove a book
            title = input("Enter the title of the book to remove: ").strip()
            print("\nController: Removing a book from the library through the model.")
            controller.remove_book(title)

        elif choice == "3":
            # View all books
            print("\nView: Displaying the current list of books in the library.")
            controller.display_books()

        elif choice == "4":
            # Exit
            print("\nExiting the Library Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


