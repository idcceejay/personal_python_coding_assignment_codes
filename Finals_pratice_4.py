class Book():
    def __init__(self, title: str, author: str, isbn: str, copies: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
    
    def __str__(self):
        return f"Title:{self.title}\nAuthor:{self.author}\nISBN:{self.isbn}\nCopies:{self.copies}"
    

class User():
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.checked_out = []


    def __str__(self):
        return f"Name:{self.name}\nEmail:{self.email}\nBooks Checked Out:[{self.checked_out}]"

class LibrarySystem():

    def __init__(self):
        self.books = []
        self.users = []
        self.checkouts = {}

    def add_book(self, book: Book):

        for b in self.books:
            if b.isbn.lower() == book.isbn.lower():
                print("Book Already Exists")
                return False
        self.books.append(book)
        print("Book Added")
        return True
    
    def add_user(self, users: User):

        for u in self.users:
            if u.email.lower() == users.email.lower():  
                print("The User already exists")
                return False
        self.users.append(users)
        print("User Added")
        return True

    def checkout_book(self, email: str, isbn: str):

        email_exist = None
        for u in self.users:
            if u.email.lower() == email.lower():
                email_exist = u
                break
            
        if email_exist is None:    
            print("User not found")
            return False


        book_exist = None
        for i in self.books:
            if i.isbn.lower() == isbn.lower():
                book_exist = i
                break

        if book_exist is None:
            print("Book does not exist")
            return False
        
    
        if book_exist.isbn in self.checkouts:
            list_of_emails = self.checkouts[book_exist.isbn]
        else:
            list_of_emails = []

        if email_exist.isbn in email_exist.checked_out:
            print("You already have this book")
            return False
        
        if len(list_of_emails) >= book_exist.copies:
            print("No Copies Available")
            return False
        
        email_exist.checked_out.append(isbn)
        list_of_emails.append(email)  
        self.checkouts[book_exist.isbn] = list_of_emails 
        print("Checkout successful")
        return True
         
    def return_book(self,email: str, isbn: str):

        user = None
        for u in self.users:
            if u.email.lower() == email.lower():
                user = u
                break
        if user is None:
            print("User not Found")
            return False
        
        book = None
        for b in self.books:
            if b.isbn.lower() == isbn.lower():
                book = b
                break
        if book is None:
            print("Book not Found")
            return False
        
        if user.isbn is not self.checked_out:
            print("Book not checked out by this user")
            return False
        
        user.check_out.remove(isbn)
        email_list = self.checkouts[book.isbn]
        email_list.remove(email)

        print("Book returned")
        return True
    
    def list_books(self):
        if len(self.books) == 0:
            print("There are no books")
            
        for b in self.books:
            print(b)
            print() 

    def list_users(self):
        if len(self.users) == 0:
            print("There are no users")
            
        for u in self.users:
            print(u)
            print()

def library_statistics(self):

    print("----- Library Statistics -----")

    # ----- TOTAL COUNTS -----
    print("Total users:", len(self.users))
    print("Total books:", len(self.books))

    # If no books, stop early
    if len(self.books) == 0:
        print("No books in the system.")
        return

    # ----- TRACKERS -----
    largest_size = -1
    largest_isbn = None

    total_checked = 0    # total number of all books checked out across all users

    # ----- FOR EACH BOOK -----
    for book in self.books:
        isbn = book.isbn

        # Count users who have this book
        if isbn in self.checkouts:
            size = len(self.checkouts[isbn])
        else:
            size = 0

        print(f"{isbn}: {size} users")

        # Track largest
        if size > largest_size:
            largest_size = size
            largest_isbn = isbn

    # ----- AVERAGE BOOKS CHECKED OUT PER USER -----
    for u in self.users:
        total_checked += len(u.checked_out)

    if len(self.users) > 0:
        avg = total_checked / len(self.users)
    else:
        avg = 0

    print(f"Average books checked out per user: {avg:.2f}")

    # ----- LARGEST BOOK -----
    if largest_isbn is not None:
        print(f"Largest book: {largest_isbn} ({largest_size} users)")
    else:
        print("Largest book: N/A")

        

def menu():
    
    system = LibrarySystem()

    while True:
        print("\n===== Library System =====")
        print("1. Add Book")
        print("2. Add User")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Users")
        print("7. Library Statistics")
        print("8. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            copies = int(input("Copies: "))
            system.add_book(Book(title, author, isbn, copies))

        elif choice == "2":
            name = input("Name: ")
            email = input("Email: ")
            system.add_user(User(name, email))

        elif choice == "3":
            email = input("User Email: ")
            isbn = input("ISBN: ")
            system.checkout_book(email, isbn)

        elif choice == "4":
            email = input("User Email: ")
            isbn = input("ISBN: ")
            system.return_book(email, isbn)

        elif choice == "5":
            system.list_books()

        elif choice == "6":
            system.list_users()

        elif choice == "7":
            system.library_statistics()

        elif choice == "8":
            print("System shutting down...")
            break

        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()