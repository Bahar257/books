import book_data

def remove_book():
    """Remove a book by ISBN or Book ID."""
    books = book_data.load_books()
    
    if not books:
        print("No books to remove.")
        return

    isbn = input("Enter ISBN or Book ID of the book to remove: ").strip()

    new_books = [book for book in books if book["isbn"] != isbn]

    if len(new_books) == len(books):
        print("No book found with that ISBN.")
        return

    book_data.save_books(new_books)
    print("Book removed successfully!")
