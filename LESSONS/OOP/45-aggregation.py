'''This is where one whole object contains references to one or more independent objects (the parts). Here, each objects exists on it's own, even if one is being referenced. it uses a 'has-a' relationship(renting)'''

class Library:
  def __init__(self, name):
    self.name = name
    self.books = []
  # Object running independently
  def intro(self):
    print('This is the library')
  # Object referencing another object through a parameter
  def add_books(self, book):
    self.books.append(book)
    print(self.books)

class Book:
  def __init__(self, name, author):
    self.name = name
    self.author = author
  # Object running on its own
  def intro(self):
    print(f'{self.name} by {self.author}')
  # Object referencing another object through a parameter
  def lib_intro(self, lib_name):
    print('The name of the library is', lib_name)


library = Library('Uniuyo Library')
book1 = Book('Alchemy of souls', '001')
book2 = Book('The precious Jewel', '002')
book3 = Book('Python book', '003')

# Objects running independently
library.intro()
book1.intro()

# Referencing to another object through an argument
library.add_books(book1.name) # renting the book
library.add_books(book2.name) # renting the book
library.add_books(book3.name) # renting the book
book1.lib_intro(library.name) # renting the name of the library

'''So, it's basically about using an indenpendent object on another object'''
'''Hint: Assign parameters to your classes, and also make use of it by applying methods'''