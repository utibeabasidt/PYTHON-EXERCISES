'''This is a decorator that is used to define a method as a property (attribute). It helps us add additional logic but using getters when reading, setters when writing, and deleter methods when deleting attributes

In a lay man, these makes a method look like a property

Note: The constructor variables must be private'''

class Rectangle:
  def __init__(self, width, height):
    # hashing the variables
    self._width = width
    self._height = height

  # getter methods to display the private varaibles
  @property
  def width(self):
    return f'{self._width:.1f}cm' # since it can be accessed here

  @property
  def height(self):
    return f'{self._height:.1f}cm' # since it can be accessed here
  
  # setter methods to modify the private varaibles using a new argument(never make the parameter name to be the same name with the method)
  @width.setter
  def set_width(self, new_width):
    self._width = new_width

  @height.setter
  def set_height(self, new_height):
    self._height = new_height

  # deleter methods to delete a private variable
  @width.deleter
  def del_width(self):
    del self._width
    print('Width has been successfully deleted')

  @height.deleter
  def del_height(self):
    del self._height
    print('Height has been successfully deleted')


rect1 = Rectangle(3, 4)

# Get width and height with the getter method
print(rect1.height) # if you try to call the private variable, it may throw an error
print(rect1.width) # if you try to call the private variable, it may throw an error

# Set item with the setter method
rect1.set_width = 2
print(rect1.width)

# deleting item with the deleter method
del rect1.del_width
del rect1.del_width

'''If you noticed, we didn't use any brackets as we do in methods. We simply called it like we are attributing it, and if we have to pass any argument, we assign it'''