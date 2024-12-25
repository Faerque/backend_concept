from models.library import Library  # Model: Manages the collection of books
from views.library_view import LibraryView  # View: Handles user-facing output
from controllers.library_controller import LibraryController  # Controller: Mediates between Model and View

# Function to display the menu to the user
def display_menu():
    """
    Displays the menu options for the Library Management System.
    """
    print("\nLibrary Management System")
    print("1. Add a Book")  # Allows the user to add a book
    print("2. Remove a Book")  # Allows the user to remove a book
    print("3. View All Books")  # Allows the user to view all books
    print("4. Exit")  # Exits the application

# Main program execution starts here
if __name__ == "__main__":
    print("Initializing the Library Management System...\n")

    # Initialize the core components of the Library Management System
    library = Library()  # Model: Manages the library's data (collection of books)
    view = LibraryView()  # View: Handles interaction with the user (display messages)
    controller = LibraryController(library, view)  # Controller: Orchestrates operations between Model and View

    print("System is ready. Follow the menu options to interact with the Library Management System.")

    # Loop to keep the program running until the user chooses to exit
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ").strip()  # Get the user's choice

        if choice == "1":
            # Add a book operation
            print("\n[Middleware]: Validating the book input...")
            title = input("Enter the title of the book: ").strip()  # Get the title of the book
            author = input("Enter the author of the book: ").strip()  # Get the author of the book
            print("[Middleware]: Validation successful.")
            print("\n[Controller]: Working to add a book to the library.")
            controller.add_book(title, author)  # Controller handles adding the book
            print("[Model]: The book data has been successfully stored in the library.")
            print("[Interceptor]: Logged action: 'Add Book'.\n")

        elif choice == "2":
            # Remove a book operation
            print("\n[Middleware]: Validating the title of the book to remove...")
            title = input("Enter the title of the book to remove: ").strip()  # Get the title of the book to remove
            print("[Middleware]: Validation successful.")
            print("\n[Controller]: Working to remove a book from the library.")
            controller.remove_book(title)  # Controller handles removing the book
            print("[Model]: If found, the book data has been successfully deleted from the library.")
            print("[Interceptor]: Logged action: 'Remove Book'.\n")

        elif choice == "3":
            # View all books operation
            print("\n[Controller]: Working to fetch all books from the library.")
            controller.display_books()  # Controller retrieves and displays the books
            print("[View]: Displayed all the books currently stored in the library.")
            print("[Interceptor]: Logged action: 'Display Books'.\n")

        elif choice == "4":
            # Exit operation
            print("\n[System]: Exiting the Library Management System. Goodbye!")
            break  # Exit the loop and terminate the program

        else:
            # Invalid choice handling
            print("\n[System]: Invalid choice. Please try again.")  # Prompt user for valid input
