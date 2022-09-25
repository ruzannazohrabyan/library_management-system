class Book:
    def __init__(self, ISBN, title, authors, publisher, published_year, pages=None):
        self.ISBN = ISBN
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.published_year = published_year
        self.pages = pages


