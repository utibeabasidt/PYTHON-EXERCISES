'''This is a way of grouping child classes in a list'''

# POLYMORPHISM BY INHERITANCE OF AN ABSTRACT CLASS
from abc import ABC, abstractmethod
class Fruits(ABC):
  @abstractmethod
  def describe(self):
    pass

class Apple(Fruits):
  def __init__(self, name):
    self.name = name
  def describe(self):
    print(self.name)

class Banana(Fruits):
  def __init__(self, name):
    self.name = name
  def describe(self):
    print(self.name)

class Grapes(Fruits):
  def __init__(self, name):
    self.name = name
  def describe(self):
    print(self.name)

fruits = [Apple('apple'), Banana('banana'), Grapes('grapes')] # Polymorphism by inheritance
for fruit in fruits:
  fruit.describe() # using the same method because all classes inherited it
