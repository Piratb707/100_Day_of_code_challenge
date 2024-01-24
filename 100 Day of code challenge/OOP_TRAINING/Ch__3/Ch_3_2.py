class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price < value.price

b1 = Book("War and Peace", "Leo tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

print(b1 == b3)
print(b1 == b2)
# print(b1 == 42)

print(b1 >= b1)
print(b2 < b1)

books = [b1, b2, b3, b4]
books.sort()
print([book.title for book in books])