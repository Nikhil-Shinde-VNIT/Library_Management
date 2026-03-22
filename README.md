# Library_Management
This Library managment project was a part of Computer programing course assesment in the first year of my B.Tech. This project particularly focuses on the basic Python usage and implementation.
This is a menu-driven Python application designed to manage library operations, including book inventory, student records, and loan history. The system uses flat-file storage to maintain data across sessions.

## Features### 
1. Book Management
   1. View Inventory: Displays a complete list of books with their unique IDs, titles, and authors.
   2. Add Books: Allows administrators to add new titles to the collection.
   3. Search: Locates specific books by name within the book.txt database.
   4. Delete: Removes book records permanently from the system.
2. Student Records
   1. Registration: Adds new students with their ID, name, and academic branch to student.txt.
   2. Student Directory: Prints a formatted list of all enrolled students.
   3. Profile Search: Finds individual student details using their unique 5-digit ID.
3. Transaction & History
   1. Book Assignment: Links a book to a student and records the transaction in history.txt.
   2. Automated Due Dates: Sets a 15-day return tenure for every issued book.
   3. Fine Calculation: Automatically calculates penalties (0.5 units per day) for late returns.
   4. Pending Submissions: Provides a bird's-eye view of all overdue books across the library.

## Technical Implementation### 
Libraries Used
  1. sys: Facilitates clean program termination via sys.exit().
  2. random: Generates random five-digit IDs for new book entries to ensure uniqueness.
  3. datetime: Handles all date-related logic, tenure tracking, and overdue calculations.

## Data Storage
  The system relies on three text-based databases:
  1. book.txt: Stores Book ID, Name, and Author.
  2. student.txt: Stores Student ID, Name, and Branch.
  3. history.txt: Stores comprehensive logs of issued books, including timestamps and deadlines.
  
