class Library:
  is_library_object = True
  def info(self):
    pass

class Pen(Library):
  def info(self):
    print("Pen")

class Book(Library):
  def info(self):
    print('Book')

class Ruler(Library):
  def info(self):
    print('Ruler')

# Polymorphism with ducktyping
class Mop: # no inheritance but similar method
  is_library_object = False
  def info(self):
    print('Mop')

library = [Pen(), Book(), Ruler(), Mop()]

for item in library:
  print(item.is_library_object)
  item.info() # using the same method because all classes had similar method, inherited or not