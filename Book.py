#creates a class called Book that has a title, author, and price
class Book:
    def __init__(self, title, author, genre, status):
        self.title = title
        self.author = author
        self.genre = ""
        self.status = "Available"   
        