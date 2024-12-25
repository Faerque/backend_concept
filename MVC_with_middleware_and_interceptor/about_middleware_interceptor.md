# **Library Management System**

## **Overview**
This project is an **enhanced version of the MVC core backend concept**, showcasing the integration of **Middleware** and **Interceptor** into the **Model-View-Controller (MVC)** architecture. The **Library Management System** is a Python-based application that allows users to dynamically add, remove, and view books. The **Middleware** ensures input validation, while the **Interceptor** provides action logging for improved system transparency and debugging.

---

## **Features**

### **Core Features:**
1. **Add a Book**:
   - Validates and stores a book with its title and author.
   - Ensures data integrity during the process.
2. **Remove a Book**:
   - Checks the validity of the book title.
   - Removes the book from the library if it exists.
3. **View All Books**:
   - Displays the list of books currently stored in the library.

### **Middleware and Interceptor Integration:**
1. **Middleware**:
   - Acts as a preprocessing layer to validate inputs (e.g., title and author).
   - Ensures that only valid data reaches the **Controller**.
2. **Interceptor**:
   - Logs every action (Add Book, Remove Book, View Books) with:
     - **Action Type** (e.g., Add, Remove, View).
     - **Timestamp**.
     - **Status** (Success or Failure).
   - Provides actionable insights for monitoring and debugging.

---

## **Architecture**

This project follows the **MVC architecture** with enhanced components:

- **Model**:
  - Represents and manages the data.
  - Classes:
    - `Library`: Manages the collection of books.
    - `Book`: Represents individual book objects.
- **View**:
  - Handles user-facing outputs.
  - Class: `LibraryView`.
- **Controller**:
  - Processes user inputs, interacts with the **Model**, and updates the **View**.
  - Class: `LibraryController`.
- **Middleware**:
  - A pre-processing layer to validate user inputs.
  - Class: `Middleware`.
- **Interceptor**:
  - A post-processing layer to log all actions for transparency.
  - Class: `Interceptor`.

---

## **Workflow**

### **Middleware:**
1. **Input Validation**:
   - Ensures book titles and authors are non-empty before processing.
   - Prevents invalid or incomplete data from reaching the Controller.
2. **When Middleware Works**:
   - Before adding a book.
   - Before removing a book.

### **Interceptor:**
1. **Action Logging**:
   - Tracks each user action with detailed logs, including timestamps and success/failure statuses.
2. **When Interceptor Works**:
   - After the **Controller** completes an action.
   - Logs actions for monitoring, debugging, and system auditing.

---

