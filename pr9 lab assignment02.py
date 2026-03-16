class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        book = Book(book_id, title)
        self.books.append(book)
        print("Book added successfully")

    def lend_book(self):
        book_id = int(input("Enter Book ID to lend: "))
        for book in self.books:
            if book.book_id == book_id and not book.issued:
                book.issued = True
                print("Book issued successfully")
                return
        print("Book not available")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))
        for book in self.books:
            if book.book_id == book_id and book.issued:
                book.issued = False
                print("Book returned successfully")
                return
        print("Invalid Book ID")

    def display_books(self):
        for book in self.books:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Issued:", book.issued)
            print("-------------------")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Lend Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.lend_book()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.display_books()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")