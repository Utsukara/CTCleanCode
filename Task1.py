#Task1 includes the following classes: Book, Library
#Book creates a class called Book that has a title, author, genre, and status that can be checked out
#Library creates a class called Library that has books sorted by genre

from Library import Library
from Book import Book

def test_library():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    book1.genre = "Fiction"
    book2 = Book("The Catcher in the Rye", "J.D. Salinger", 9.99)
    book2.genre = "Fiction"
    book3 = Book("1984", "George Orwell", 8.99)
    book3.genre = "Science Fiction"
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)
    assert library.getBooksByGenre("Fiction") == [book1, book2]
    assert library.getBooksByGenre("Science Fiction") == [book3]
    assert library.getGenres() == ["Fiction", "Science Fiction"]
    library.changeStatus(book1, "Checked Out")
    assert book1.status == "Checked Out"
    library.changeStatus(book1, "Available")
    assert book1.status == "Available"
    library.exportLibrary("library.txt")
    library2 = Library()
    library2.importLibrary("library.txt")
    assert str(library) == str(library2)



def librarian_interface():
    library = Library()
    library.importLibrary("library.txt")
    while True:
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. Display books by genre")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            genre = input("Enter the genre: ")
            price = float(input("Enter the price: "))
            book = Book(title, author, price)
            book.genre = genre
            library.addBook(book)
        elif choice == "2":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            book = None
            for b in library.books:
                if b.title == title and b.author == author:
                    book = b
                    break
            if book == None:
                print("Book not found")
            else:
                library.removeBook(book)
        elif choice == "3":
            print(library)
        elif choice == "4":
            genre = input("Enter the genre: ")
            print(library.getBooksByGenre(genre))
        elif choice == "5":
            library.exportLibrary("library.txt")
            break
        else:
            print("Invalid choice")



def user_interface():
    library = Library()
    library.importLibrary("library.txt")
    while True:
        print("1. Display all books")
        print("2. Display books by genre")
        print("3. Check out a book")
        print("4. Check in a book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(library)
        elif choice == "2":
            genre = input("Enter the genre: ")
            print(library.getBooksByGenre(genre))
        elif choice == "3":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            book = None
            for b in library.books:
                if b.title == title and b.author == author:
                    book = b
                    break
            if book == None:
                print("Book not found")
            else:
                library.changeStatus(book, "Checked Out")
        elif choice == "4":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            book = None
            for b in library.books:
                if b.title == title and b.author == author:
                    book = b
                    break
            if book == None:
                print("Book not found")
            else:
                library.changeStatus(book, "Available")
        elif choice == "5":
            library.exportLibrary("library.txt")
            break
        else:
            print("Invalid choice")


def main():
    #test_library()
    #librarian_interface()
    user_interface()

if __name__ == "__main__":
    main()