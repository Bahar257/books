import book_data

def add_book():
    """Add a new book to the store."""
    books = book_data.load_books()

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN or Book ID: ").strip()
    genre = input("Enter genre: ").strip()
    
    try:
        price = float(input("Enter price: "))
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        quantity = int(input("Enter quantity in stock: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Prevent duplicate ISBNs
    if any(book["isbn"] == isbn for book in books):
        print("Error: A book with this ISBN already exists!")
        return

    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "genre": genre,
        "price": price,
        "quantity": quantity
    }

    books.append(new_book)
    book_data.save_books(books)
    print(f"Book '{title}' added successfully!")
