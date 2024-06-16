## Overview ##
# The bookstore_main program has been split up into three modules to try and keep the main program clean.
# The menu.py module contains the top-level menu functions, which call seperate functions to get information from the user and pass that information into the database.
# The user.py module contains the functions that interact with the user.
# The db.py module contains the functions that interact with the database.


## Imports ##
import menu
import db
            
## Main Code ##

db.create()

# Introduction.
print('\nBookstore Stock Keeping Program')

# Main menu.
while True:
    user_input = input('''\nPlease select from one of the following options:
1 - Register a book
2 - Update book information
3 - Delete a book
4 - Search for a book
5 - Show all books
0 - Exit the program
: ''')

    # Register a book.
    if user_input == '1':
        menu.register_book()
    
    # Update a book.
    elif user_input == '2':
        menu.update_book()

    # Delete a book.
    elif user_input == '3':
        menu.delete_book()

    # Search for a book.
    elif user_input == '4':
        menu.find_book()

    # Show all the books in the database.
    elif user_input == '5':
        menu.show_books()

    # Exit program.
    elif user_input == '0':
        print('\nLogging off...\n')
        exit()