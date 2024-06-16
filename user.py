# Contains all the functions that interact with the user.

# Prints the book contained in a list.
def print_books(search_term, book_info):
    print(f'\nBooks matching the search term \'{search_term}\':')
    print('\nID : Title : Author : Quantity in stock')
    for book in book_info:
        print(f'{book[0]} : {book[1]} : {book[2]} : {book[3]}')

# Filters a list of search results by ID.
def filter_search(search_term, search_results):
    filtered_search_results = []
    # Prints the books contained in the search_results list.
    print_books(search_term, search_results)
    # Allows the user to search for a specific book by ID if the results return multiple books.
    while True:
        user_input = input(f'''\nYour search for '{search_term}' returned {len(search_results)} results.
Please select the book you wish to update by entering its ID number.
: ''')
        # Checks the user input is a valid ID.
        try:
            int(user_input)
        except ValueError:
            print("\nYou did not enter an ID number.")
            continue
        id_selection = int(user_input)   
        # Searches the tuples in search_results for that ID number. 
        for book in search_results:
            for field in book:
                if id_selection == field:
                    # Appends that book to filtered_search_results.
                    filtered_search_results.append(book)
        # If the ID number doesn't match anything.
        if len(filtered_search_results) == 0:
            print("\nYou did not enter a valid ID number.")
            continue
        else:
            # Converts the list of tuples to just a tuple because there will only be one result.
            filtered_search_result = filtered_search_results[0]
            return filtered_search_result    

# Gets information from the user about a new book.
def get_new_book_info():
    # Creates new empty list.
    new_book_info = []
    # Gets and adds the book title to the list.
    new_book_title = input('''\nPlease enter the title of the book you wish to add.
: ''')
    new_book_info.append(new_book_title)
    # Gets and adds the book's author to the list.
    new_book_author = input('''Please enter the author of the book you wish to add.
: ''')
    new_book_info.append(new_book_author)
    # Gets, checks for int and adds the quantity of books in stock to the list.
    while True:
        new_book_qty = input('''Please enter the quantity of books in stock.
: ''')
        try:
            int(new_book_qty)
        except ValueError:
            continue
        new_book_qty = int(new_book_qty)
        break
    new_book_info.append(new_book_qty)
    # Returns the list of book information.
    return new_book_info

# Gets information from the user about an updated book's title.
def get_updated_title_info(book_to_change_info):
    while True:
        print(f'\nThe current title of the book is {book_to_change_info[1]}.')
        menu = input('''Enter 'Y' to change it or 'N' to move on to the next field.
: ''').lower()
        if menu == 'y':
            updated_book_title = input('''\nPlease enter the new title of the book.
: ''')
            return updated_book_title
        elif menu == 'n':
            return book_to_change_info[1]
        else:
            print('\nThe command you entered was not recognised.')

# Gets information from the user about an updated book's author.
def get_updated_author_info(book_to_change_info):
    while True:
        print(f'\nThe current author of the book is {book_to_change_info[2]}.')
        menu = input('''Enter 'Y' to change it or 'N' to move on to the next field.
: ''').lower()
        if menu == 'y':
            updated_book_author = input('''\nPlease enter the author of the book.
: ''')
            return updated_book_author
        elif menu == 'n':
            return book_to_change_info[2]
        else:
            print('\nThe command you entered was not recognised.') 

# Gets information from the user about an updated book's quantity.
def get_updated_qty_info(book_to_change_info):
    while True:
        print(f'\nThe number of units in stock of this book is {book_to_change_info[3]}.')
        menu = input('''Enter 'Y' to change it or 'N' to move on to the next field.
: ''').lower()
        if menu == 'y':
            while True:
                updated_book_qty = input('''\nPlease enter the number of books in stock.
: ''')
                try:
                    int(updated_book_qty)
                except ValueError:
                    print('\nThe number you entered was invalid.')
                    continue
                updated_book_qty = int(updated_book_qty)
                return updated_book_qty
        elif menu == 'n':
            return book_to_change_info[3]
        else:
            print('\nThe command you entered was not recognised.')

# Gets information from the user about updates for a book.
def get_updated_book_info(book_to_change_info):
    updated_book_info = []
    # Adds the same id number to the new info list.
    updated_book_info.append(book_to_change_info[0])
    # Get new title info.
    updated_book_title = get_updated_title_info(book_to_change_info)
    updated_book_info.append(updated_book_title)
    # Get new author info.
    updated_book_author = get_updated_author_info(book_to_change_info)
    updated_book_info.append(updated_book_author)
    # Get new quantity info.
    updated_book_qty = get_updated_qty_info(book_to_change_info)
    updated_book_info.append(updated_book_qty)
    # Adds the search term onto the updated_book_info list.
    updated_book_info.append(book_to_change_info[4])
    # Return the updated book information as a tuple.
    updated_book_info_tup = tuple(updated_book_info)
    return updated_book_info_tup