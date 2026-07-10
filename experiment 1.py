class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def borrow(self, book):
        if book.available:
            book.available = False
            print(book.title, "borrowed successfully.")
        else:
            print(book.title, "is not available.")

    def return_book(self, book):
        book.available = True
        print(book.title, "returned successfully.")

# Create two books
book1 = Book("Python")
book2 = Book("DBMS")

library = Library()

print("Available Books:")
print("1. Python")
print("2. DBMS")

choice = int(input("Enter book number (1 or 2): "))
action = input("Enter action (borrow/return): ").lower()

if choice == 1:
    book = book1
elif choice == 2:
    book = book2
else:
    print("Invalid book number.")
    exit()

if action == "borrow":
    library.borrow(book)
elif action == "return":
    library.return_book(book)
else:
    print("Invalid action.")
    
