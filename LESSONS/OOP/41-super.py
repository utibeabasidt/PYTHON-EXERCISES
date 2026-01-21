'''This is a function that allows a child class to reuse methods from a parent class. We are not basically using the arguments of the parent class, we are simply just passing our own arguments into an already existing method.'''

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled

# Inherit from Shape
class Circle (Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled) # passing its own arguments to an already existing method

class Square(Shape):
  def __init__(self, color, is_filled, width):
    super().__init__(color, is_filled) # passing its own arguments to an already existing method
    self.width = width

# Inherit from Square
class Triangle(Square):
  def __init__(self, color, is_filled, width, height):
    super().__init__(color, is_filled, width) # passing its own arguments to an already existing method
    self.height = height

Shape('red', True) # Super class
Square('red', False, 30) # Sub class resuing the methods in the parent to include its own arguments
