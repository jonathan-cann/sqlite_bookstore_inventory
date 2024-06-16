# Contains all the top level menu functions.

## Imports ##

import db
import user

## Functions ##

# Registers a book in the database.
def register_book():
    # Get new book information from the user.
    new_book_info = user.get_new_book_info()
    # Confirm the user wants to add the book to the database.
    while True:
        user_input = input(f'''\nDo you wish to add {new_book_info[0]} by {new_book_info[1]} to the database? Enter 'Y' to confirm or 'N' to cancel the process.
: ''').lower()
        # If yes, add the book.
        if user_input == 'y': 
            db.add_book(new_book_info)
            return
        # If no, exit the function.
        elif user_input == 'n':
            return
        else:
            print('\nThe command you entered was not recognised.')

# Updates a book in the database.
def update_book():
    # Search the db for book information relating to a search term.
    current_book_info = db.search('update')
    # Checks if the user wants to update the book.
    while True:
        user_input = input(f'''\nDo you wish to update {current_book_info[1]} by {current_book_info[2]}? Enter 'Y' to confirm or 'N' to cancel the process.
: ''').lower()
        # If yes, get new info from the user.
        if user_input == 'y':
            updated_book_info = user.get_updated_book_info(current_book_info)
            # If the new info is the same as the old info.
            if current_book_info == updated_book_info:
                # Do nothing.
                print('\nThe new information entered is the same as the old information. No changes will be made to the database.')
            else:
                # Update the book.
                db.update_book(updated_book_info)
                print(f'\nThe book with ID {updated_book_info[0]} has been successfully updated.')
            return
        # If no, exit the function.
        elif user_input == 'n':
            return
        else:
            print('\nThe command you entered was not recognised.')

# Deletes a book.
def delete_book():
    # Search the db for book information relating to a search term.
    search_result = db.search('delete')
    # Check if the user wants to delete the book.
    while True:
        user_input = input(f'''\nDo you really wish to delete {search_result[1]} by {search_result[2]}?
Once deleted, the information cannot be recovered. Enter 'Y' to confirm or 'N' to cancel the process.
: ''').lower()
        # If yes, delete the book.
        if user_input == 'y':
            db.delete_book(search_result)
            return
        # If no, exit the function.
        elif user_input == 'n':
            return
        else:
            print('\nThe command you entered was not recognised.')

# Prints a formatted list of specific book information.
def find_book():
    # Search the db for book information relating to a search term.
    search_results = db.search('search')
    # Print the search results.
    user.print_books(search_results[0][4], search_results)

# Prints a formatted list of all books.
def show_books():
    db.show_all_books()