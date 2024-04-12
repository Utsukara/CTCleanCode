#create a class called Library that has books sorted by genre
import Book

class Library:
    def __init__(self):
        self.books = []
        self.genres = []
        self.booksByGenre = {}

    def addBook(self, book):
        self.books.append(book)
        if book.genre not in self.genres:
            self.genres.append(book.genre)
            self.booksByGenre[book.genre] = []
        self.booksByGenre[book.genre].append(book)

    def removeBook(self, book):
        self.books.remove(book)
        self.booksByGenre[book.genre].remove(book)

    def getBooksByGenre(self, genre):
        return self.booksByGenre[genre]
    
    def getGenres(self):
        return self.genres
    
    def changeStatus(self, book, status):
        book.status = status

    def importLibrary(self, filename):
        f = open(filename, "r")
        for line in f:
            try:
                line = line.strip()
                parts = line.split(",")
                title = parts[0]
                author = parts[1]
                genre = parts[2]
                status = parts[3]
                book = Book.Book(title, author, genre, status)
                book.genre = genre
                self.addBook(book)
            except TypeError:
                print("Error reading line: " + line)
        f.close()



    def exportLibrary(self, filename):
        f = open(filename, "w")
        for book in self.books:
            f.write(book.title + "," + book.author + "," + book.genre + "," + book.status + "\n")
        f.close()

    def __str__(self):
        result = ""
        for book in self.books:
            result += book.title + " by " + book.author + " (" + book.genre + ") - " + book.status + "\n"
        return result