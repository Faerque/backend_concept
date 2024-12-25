# Library Management System

## Overview
The **Library Management System** is a Python-based project demonstrating core backend concepts with a focus on **Middleware** and **Interceptor** integration. This system follows the **Model-View-Controller (MVC)** architecture and allows users to add, remove, and view books dynamically. Middleware and Interceptor are key components that ensure input validation and action logging, respectively.

---

## Features

### Core Features:
1. **Add a Book**: Validates and stores a book with its title and author.
2. **Remove a Book**: Ensures the title is valid and removes the book if it exists.
3. **View All Books**: Displays the list of books in the library.

### Middleware and Interceptor Integration:
1. **Middleware**:
   - Validates user inputs (e.g., title and author) before processing.
   - Ensures data integrity and prevents invalid data from reaching the Controller.
2. **Interceptor**:
   - Logs actions (e.g., Add Book, Remove Book) with timestamps and status.
   - Tracks successful and failed operations for debugging and auditing.

---

## Architecture

This project follows the **Model-View-Controller (MVC)** architecture:

- **Model**: Manages the data (e.g., books in the library).
  - Classes: `Library` (stores books), `Book` (represents a single book).
- **View**: Handles user interaction and displays output.
  - Class: `LibraryView`.
- **Controller**: Processes user input, interacts with the Model, and updates the View.
  - Class: `LibraryController`.
- **Middleware**: Validates user inputs to ensure data integrity.
  - Class: `Middleware`.
- **Interceptor**: Logs all actions with timestamps and details.
  - Class: `Interceptor`.

---

## Workflow

### **Middleware**:
1. **Validation**:
   - Validates inputs (e.g., title and author) before processing.
   - Prevents invalid or empty data from being passed to the Controller.
2. **When Middleware Works**:
   - Before adding a book.
   - Before removing a book.

### **Interceptor**:
1. **Logging**:
   - Logs all actions (Add Book, Remove Book, View Books) with details like:
     - Action Type.
     - Timestamp.
     - Status (Success/Failure).
2. **When Interceptor Works**:
   - After the Controller completes an action.
   - Provides real-time action tracking for debugging or auditing.

---

## Example Workflow

### **Add a Book Workflow**:
1. User selects **Add a Book**.
2. **Middleware** validates the title and author.
   - If invalid, the process stops, and an error message is displayed.
   - If valid, the Controller proceeds.
3. **Controller** sends the data to the **Model** for storage.
4. **Model** stores the book.
5. **Interceptor** logs the action as `SUCCESS` or `FAILURE`.

### **Remove a Book Workflow**:
1. User selects **Remove a Book**.
2. **Middleware** validates the title.
3. **Controller** checks with the Model.
4. **Model** removes the book if found.
5. **Interceptor** logs the action with the result.

---


