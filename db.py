# Contains all the functions that interact with the database.

## Imports ##

import sqlite3
import user

## Functions ##

# Creates a database if one does not already exist.
def create():
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS book(
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT,
                            qty INTEGER)''')
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Searches the db for books matching the parameter. Returns a list of tuples.
def get_info(search_term):
    db_info = []
    book_info = []
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM book WHERE 
                       id = ? OR title = ? OR author = ?''',
                       (search_term, search_term, search_term))
        for row in cursor:
            db_info.append(row)
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    # Adds the search term to the end of each tuple.
    for book in db_info:
        temp = list(book)
        temp.append(search_term)
        book = tuple(temp)
        book_info.append(book)
    # Returns a list of tuples containing book information.
    return book_info

# Gets a search term from the user and returns results from the db, depending on what the function is being used for.
def search(purpose):
    while True:
        # If using the function to purely search for books.
        if purpose == 'search':
            user_input = input(f'''\nPlease enter a search term related to a book. You can search by ID, title or author.
: ''')
            search_results = get_info(user_input)
            if len(search_results) == 0:
                print('\nYour search did not return any results. Please try again.')
            else:
                return search_results
        # If using the function to search for books to delete or update them.
        else:
            user_input = input(f'''\nPlease enter a search term related to the book you wish to {purpose}.
You can search by ID, title or author.
: ''')
            search_results = get_info(user_input)
            if len(search_results) == 0:
                print('\nYour search did not return any results. Please try again.')
            elif len(search_results) == 1:
                search_result = search_results[0]
                return search_result
            else:
                search_result = user.filter_search(user_input, search_results)
                return search_result
            
# Gets a list of IDs already used in the db.
def get_ids():
    id_list = []
    try:
        # Connect to db.
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        # Get a list of ids already registered in the db.
        cursor.execute('SELECT id FROM book')
        for row in cursor:
            for id in row:
                id_list.append(id)
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    return id_list

# Gets a list of book information based on a search term.
def get_book_info(search_term):
    book_info = []
    try:
        # Connect to db.
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        # Gets information about rows that contain the search term.
        cursor.execute('''SELECT * FROM book WHERE 
                       id = ? OR title = ? OR author = ?''',
                       (search_term, search_term, search_term))
        for row in cursor:
            for item in row:
                book_info.append(item)
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    # Returns the list of books.
    return book_info

# Adds a book to the db containing info from a list.
def add_book(book_info):
    new_id = 3001
    # Gets the current list of IDs from the db.
    db_id_list = get_ids()
    # Gets a unique ID for the new book.
    for id in db_id_list:
        if new_id == id:
            new_id += 1
        else:
            break
    # Add the new book to the db.
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO book
                       (id, title, author, qty)
                       VALUES(?, ?, ?, ?)''',
                       (new_id, book_info[0], book_info[1], book_info[2])
        )
        db.commit()
        print(f'\n{book_info[0]} by {book_info[1]} has been successfully added to the database.')
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Updates the information of a book using information from a list.
def update_book(updated_book_info):
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('''UPDATE book SET
                       title = ?, author = ?, qty = ?
                       WHERE id = ?''',
                       (updated_book_info[1], updated_book_info[2], updated_book_info[3], updated_book_info[0])
        )
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Shows a formatted list of all books to the user.
def show_all_books():
    print('\nBooks registered:')
    print('ID : Title : Author : Quantity in stock')
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM book')
        for row in cursor:
            print(f'{row[0]} : {row[1]} : {row[2]} : {row[3]}')
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Deletes a book from the db.
def delete_book(book_info):
    book_id = book_info[0]
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM book WHERE
                       id = ?''',
                       (book_id,))
        db.commit()
        print(f'\n{book_info[1]} by {book_info[2]} has been successfully deleted from the database.')
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()