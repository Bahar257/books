import book_data

def view_books():
    """Display all books in the store."""
    books = book_data.load_books()
    
    if not books:
        print("No books available.")
        return
    
    print("\nList of Books:")
    print("=" * 50)
    for book in books:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Genre: {book['genre']}")
        print(f"Price: ${book['price']:.2f}")
        print(f"Quantity: {book['quantity']}")
        print("-" * 50)
