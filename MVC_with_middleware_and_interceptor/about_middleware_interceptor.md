# Library Management System

## Overview
This project is an **enhanced version of the MVC core backend concept**, showcasing the integration of **Middleware** and **Interceptor** into the **Model-View-Controller (MVC)** architecture. The **Library Management System** is a Python-based application that allows users to dynamically add, remove, and view books. The **Middleware** ensures input validation, while the **Interceptor** provides action logging for improved system transparency and debugging.

---

## Features

### Core Features:
1. **Add a Book**: Validates and stores a book with its title and author.
2. **Remove a Book**: Ensures the title is valid and removes the book if it exists.
3. **View All Books**: Displays the list of books currently in the library.

### Middleware and Interceptor Integration:
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

## Architecture

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

## Workflow

### Middleware:
1. **Input Validation**:
   - Ensures book titles and authors are non-empty before processing.
2. **When Middleware Works**:
   - Before adding a book.
   - Before removing a book.

### Interceptor:
1. **Action Logging**:
   - Tracks each user action with detailed logs, including timestamps and success/failure statuses.
2. **When Interceptor Works**:
   - After the **Controller** completes an action.
   - Logs actions for monitoring, debugging, and system auditing.

---

## Example Workflow

### Add a Book Workflow:
1. User selects **Add a Book**.
2. **Middleware** validates the title and author.
   - If invalid, the process stops, and an error message is displayed.
   - If valid, the **Controller** proceeds.
3. **Controller** sends the data to the **Model** for storage.
4. **Model** stores the book.
5. **Interceptor** logs the action with a `SUCCESS` or `FAILURE` status.

---
