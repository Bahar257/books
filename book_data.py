import json
import os

BOOKS_FILE = "books.json"

def load_books():
    """Load books from the JSON file."""
    if not os.path.exists(BOOKS_FILE):
        return []
    
    with open(BOOKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_books(books):
    """Save books to the JSON file."""
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)
