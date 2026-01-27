'''Also knowns as dunder methods(__methodname__), they are automatically called by many of python's built-in operations e.g printing an object, logical operations, etc. They allow developers to define or customise the behaviour or objects
E.g are init, str, add, sub, less than, greater than, contains(membership), get item(indexing)'''

class Book:
  # Initialising Objects
  def __init__(self, title, author, no_of_pages):
    self.title = title
    self.author = author
    self.no_of_pages = no_of_pages

  # Returns the string representation of the object while printed directly
  def __str__(self):
    return f'{self.title} by {self.author}'
  
  # Returns the boolean value of checking if each object's attributes are the same (you can make use of and and or incase you want to check many conditions)
  def __eq__(self, other):
    return self.title == other.title # boolean value if their titles are the same or not
  
  # Returns a boolean value if one object is less than the other
  def __lt__ (self, other):
    return self.no_of_pages < other.no_of_pages # be careful to use only less than sign here
  
  # Returns a boolean value if one object is greater than the other
  def __gt__ (self, other):
    return self.no_of_pages > other.no_of_pages # be careful to use only greater than sign here

  # Returns the addition of two objects alone
  def __add__ (self, other):
    return self.no_of_pages + other.no_of_pages
  
  # Returns the subtaction of two objects alone
  def __sub__(self, other):
    return self.no_of_pages - other.no_of_pages
  
  ## returns membership operator (in or not in) between a keyword and an object attribute (be careful with how you use in and not in). You can also play with and and not too. You can use this method once
  def __contains__(self, keyword):
    return keyword in self.title
  
  # RETURNING OBJECT ATTRIBUTES BY INDEXING
  def __getitem__(self, key):
    if key == 'title':
      return self.title
    elif key == 'author':
      return self.author
    elif key == 'number':
      return self.no_of_pages
    else:
      return(f'Key \'{key}\' was not found')
    
  
# Automatically calling the __init__ method by creating your objects
book1 = Book('Java Book', 'Java Java', 300)
book2 = Book('Python Book', 'Python Python', 500)
book3 = Book('Javascript Book', 'Javascript Javascript', 100)
book4 = Book('Rust Book', 'Rust Rust', 200)
book5 = Book('Rust Book', 'Rusty Rusty', 250)

# Automatically using the format in __str__ to print the object once it is direct(doesn't require calling the attribute of the object)
print(book1)
print(book2)
print(book3)
print(book4)
print(book5)

## Note: We are only using two objects for each operator (e.g 1 == 2, 1 + 2...)

# self == another book (checking if their self.title are the same)
print(book1 == book2) # False, because their title are not identical
print(book4 == book5) # True, because ALL their title are identical

# self less than the other
print(book1 < book2) # true

# self greater than the other
print(book2 > book3) # true

# add two books alone together
print(book1 + book2)

# Subtract one book from another alone
print(book1 - book2)

# MEMBERSHIP
print('Java' in book4) # false, cuz the keyword is not in the title of book4

# Getting an attribute by INDEXING
print(book1['number']) # since the key is number, print the number of pages of book1
print(book1['audio']) # since the key is number, print the number of pages of book1

