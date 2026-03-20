# Library Management System - Code Documentation
## General Description
This project is a console application developed in Python that allows managing books within a library.

The system is designed in a modular way, separating responsibilities into different files to improve code organization and maintenance.

## How does the code work?
The system is divided into modules, where each file fulfills a specific function within the program.

## Module Explanation
### models.py
Contains the main data structure:

books = [ ]

This list store all books as dictionaries.

Each book has the following structure:

{ "title": str, "year": int, "author": str, "status": str }

### validations.py
Responsible for validating all user inputs

#### Main funtions:
* validation_menu_option() -> Validates the menu option
* validatio_book_name() -> Allows only letters in the book name
* validation_book_year() -> Validates that the year is a number between 0 and 2026
* validation_book_author() → Validates the author's name
* validation_status() → Only allows:
  * "available"
  * "borrowed"
* validation_update() → Verifies that the selected book exists

Uses recursion to repeat input it is valid.

### services.py
Contains the main system logic 
* register_book()
 * Requests book data
 * Returns a dictionary with the information
* show_books()
 * Uses enumerate() to list books with numbering
 * Displays all book data
* update_book()
 * Allows modifying:
   * Title
   * Year
   * Author
 * Updates the book using its position in the list
* book_status()
 * Changes the book status (available/borrowed)
* erase_book()
  * Deletes a book using pop()
  * Allows deleting multiple books

### menu.py
This is the entry point of the program

Runs the system by calling the menu:

from menu import menu

menu()

## Program Flow
* main.py is executed
* The menu is displayed
* The user selects ann option
* The input is validated
* The corresponding function in services.py is executed
* Data is updated in models.py

## Important Behaviors
* The program runs continuously until "Exit" is selected
* Error handling with try/except
* Does not allow operations if there are no books
* Prevents invalid inputs

## Key Concepts Used
* Lists and dictionaries
* Functions and modularization
* Loops ( while, for )
* Conditionals (if, match - case )
* Error handling ( try/except )
* Data validation
