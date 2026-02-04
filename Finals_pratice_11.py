class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def description(self):
        return f"Title: {self.title} | Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []   # list of Book objects

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if len(self.books) == 0:
            print("Library is empty.")
        else:
            print("Here are all the books:")
            for b in self.books:
                print(b.description())

    def find_author(self, name: str):
        """Return a list of titles written by this author (case-insensitive)."""
        results = []
        for b in self.books:
            if b.author.lower() == name.lower():
                results.append(b.title)
        return results


if __name__ == "__main__":
    library = Library()

    while True:
        option = input(
            "\n[Library System]\n"
            "1. Add book\n"
            "2. List books\n"
            "3. Search by author\n"
            "4. Quit\n"
            "Enter option: "
        )

        if option == "1":
            title = input("Title: ")
            author = input("Author: ")
            book_obj = Book(title, author)
            library.add_book(book_obj)
            print("Book added.")

        elif option == "2":
            library.list_books()

        elif option == "3":
            name = input("Author to search for: ")
            titles = library.find_author(name)

            if len(titles) == 0:
                print("No books by that author.")
            else:
                print("Books by", name + ":")
                for t in titles:
                    print("-", t)

        elif option == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")
 