class Book():
    def __init__(self, title: str, author: str, year: int, copies: int):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
    
    def checkout(self):
        if self.copies == 0:
            print("There is no copies to remove.")
        else:
            self.copies -= 1
            print("Book has been checked out")
    
    def return_book(self):
        self.copies += 1
        print("Book returned")
    
    def __str__(self,):
        return f"{self.title} by {self.author} ({self.year}) — Copies: {self.copies}"


class Member():
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.check_out = []

    def borrow(self, title: str):
        self.check_out.append(title)

    def return_book(self, title: str):
        if title in self.check_out:
            self.check_out.remove(title)
        else:
            print("Member does not have this book checked out")

    def __str__(self):
        if len(self.check_out) == 0:
            books = "no books"
        else:
            books = ""
            for title in self.check_out:
                books += title + " "
        return f"{self.name} with the email of {self.email} has checkout {books}"
    



class Library():
    def __init__(self):
        
        self.books = []
        self.members = []
    
    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)
    
    def checkout_book(self, member_name: str, title: str):
        member_exist = None

        for m in self.members:
            if m.name.lower() == member_name.lower():
                member_exist = m
                break
            if member_exist is None:
                print('Member not found')
                return
            
        book_exist = None
        for b in self.books:
            if b.title.lower() == title.lower():
                book_exist = b
                break

            if book_exist is None:
                print('Book is not found')
                return
            
            if book_exist.copies == 0:
                print("No Copies avaiable")
                return
            
            book_exist.checkout()
            member_exist.borrow(book_exist.title)
    
    def return_book(self, member_name: str, title: str):
        member_exist = None

        for m in self.members:
            if m.name.lower() == member_name.lower():
                member_exist = m
                break
            if member_exist is None:
                print("Member not found")
                return


        book_exist = None

        for b in self.books:
            if b.title.lower() ==  title.lower():
                book_exist = b
                break
            if book_exist is None:
                print("Book is not found")
                return 
        if title not in member_exist.checkout():
            print("Member does not have this book")
            return
        
        book_exist.return_book()
        member_exist.return_book(title)

    

lib = Library()

while True:
    

    option = input("""
                    1. Add Book
                    2. Add Member
                    3. Checkout
                    4. Return
                    5. List books
                    6. List Members
                    7. Quit""")
    
    if option == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = int(input("Enter year: "))
        copies = int(input("Enter number of copies: "))
        book = Book(title,author,year,copies)
        lib.add_book(book)
        print(f"Book {title} has been added")

    elif option == "2":
        name = input("Member Name:")
        email = input("Enter Emmail: ")
        member = Member(name,email)
        lib.add_member(member)
        print(f"{name} has been added")
    
    elif option == "3":
        title = input("What book to checkout: ")
        member = input("Member name")
        lib.checkout_book(member, title)
    
    elif option == "4":
        title = input("What book to return: ")
        member = input("Member Name: ")
        lib.return_book(member, title)
        

    elif option == "5":
        if len(lib.books) == 0:
            print("There is no book")
        else:
            for b in lib.books:
                print(b)
    
    elif option == "6":
        if len(lib.members) == 0:
            print("Member does not exist")
        else:
            for m in lib.members:
                print(m)
        
    elif option == "7":
        print("Goodbye")
        break
    else:
        print("Invalid option. Try Again. ")

        
