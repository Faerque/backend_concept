# **Library Management System**

## **Overview**
The **Library Management System** is a Python-based application designed to demonstrate the core concepts of **Model-View-Controller (MVC)** architecture in backend development. This project showcases how to effectively separate concerns into modular components, ensuring a maintainable and scalable application.

Users can dynamically add, remove, and view books in a simulated library, making this a great learning tool for understanding the essentials of backend design patterns.

---

## **Features**
This system provides the following features:

1. **Add a Book**:
   - Users can add a book to the library by entering its title and author.
   - Ensures new entries are correctly processed and stored.

2. **Remove a Book**:
   - Allows users to remove a book by its title, provided it exists in the library.
   - Confirms successful removal with a clear message.

3. **View All Books**:
   - Displays the list of all books currently stored in the library.
   - Presents the data in a user-friendly format.

---

## **Architecture**

This project follows the **Model-View-Controller (MVC)** architecture, where each component plays a specific role to maintain clarity and separation of concerns:

### **1. Model**
The **Model** represents the data and business logic of the application. It is responsible for:
- **Managing the data**: Adding, removing, and retrieving books.
- **Ensuring data integrity**: Maintaining the structure and rules of the library.

#### **Classes**:
- **`Library`**:
  - Acts as a data store for managing the collection of books.
  - Provides methods to add, remove, and fetch books.
- **`Book`**:
  - Represents individual book objects with attributes like `title` and `author`.

---

### **2. View**
The **View** is the user-facing component of the application. It:
- **Handles output**: Displays data or system messages to the user.
- **Keeps the interface clean**: Ensures users can easily understand the presented information.

#### **Class**:
- **`LibraryView`**:
  - Displays success or error messages.
  - Shows the current list of books in the library.

---

### **3. Controller**
The **Controller** acts as the bridge between the **Model** and the **View**. It:
- **Processes user inputs**: Interprets commands like "add book" or "view books."
- **Manages interactions**: Coordinates between the Model and the View to execute actions and provide feedback.

#### **Class**:
- **`LibraryController`**:
  - Receives user input, interacts with the Model to process data, and uses the View to display results.

---

## **How It Works: Workflow**

Here’s a step-by-step explanation of how the system handles each operation:

### **1. Add a Book**
- **User Action**: The user chooses to add a book and enters the title and author.
- **Controller**:
  - Processes the input.
  - Sends the data to the Model to create a new book entry.
- **Model**:
  - Adds the new book to the library.
  - Confirms the operation.
- **View**:
  - Displays a success message: “Book added successfully.”

---

### **2. Remove a Book**
- **User Action**: The user chooses to remove a book by specifying its title.
- **Controller**:
  - Validates the input.
  - Checks with the Model if the book exists.
- **Model**:
  - Removes the book from the library if found.
  - Notifies the Controller about the outcome.
- **View**:
  - Displays a success message if the book is removed or an error message if the book is not found.

---

### **3. View All Books**
- **User Action**: The user selects the option to view all books.
- **Controller**:
  - Requests the list of books from the Model.
- **Model**:
  - Fetches the list of books.
- **View**:
  - Displays the list in a user-friendly format.

---

## **Why Use MVC?**

The **MVC architecture** is a proven design pattern that offers several advantages:
1. **Separation of Concerns**:
   - Each component (Model, View, Controller) focuses on a single responsibility, making the application easier to understand and maintain.
2. **Scalability**:
   - New features can be added to individual components without affecting others.
3. **Reusability**:
   - Models and Views can be reused across different parts of the application.
4. **Debugging**:
   - Issues are easier to locate because of the clear boundaries between components.

---
