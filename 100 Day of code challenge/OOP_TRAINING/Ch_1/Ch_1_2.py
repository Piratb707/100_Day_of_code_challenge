
class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("The Catcher in the Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washongton Post")
n2 = Newspaper("The New York Times")

# print(type(b1))
# print(type(n1))

# print(type(b1) == type(b2))
# print(type(b1) == type(n2))

# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(n2, Book))
print(isinstance(n2, object))