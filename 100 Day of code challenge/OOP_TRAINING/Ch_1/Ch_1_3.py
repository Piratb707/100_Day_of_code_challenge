
class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    @classmethod
    def get_book_type(cls):
        return cls.BOOK_TYPES

    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist


    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

print("Book types: ", Book.get_book_type())

b1 = Book("Title1","HARDCOVER")
b2 = Book("Title1","PAPERBACK")

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)

print(thebooks)

