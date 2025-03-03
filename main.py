import add_book
import view_books
import remove_book

def main():
    """Main menu for the Book Store Management System."""
    while True:
        print("\n📚 Book Store Management System")
        print("=" * 40)
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book.add_book()
        elif choice == "2":
            view_books.view_books()
        elif choice == "3":
            remove_book.remove_book()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please enter a number between 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
