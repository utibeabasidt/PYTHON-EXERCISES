'''This are parent class that has abstract methods (Methods that cannot be ran from a parent object except a child class/object inherits the parent, modify the abstract methods, uses and implements it)'''

'''From abstract based classes, import abstract based class and abstract method'''

from abc import ABC, abstractmethod

# Parent class
class Vehicle(ABC): # this means that we won't be able to create an object from this class
  # making the methods incomplete by making them abstract
  @abstractmethod
  def go(self):
    pass
  @abstractmethod
  def stop(self):
    pass
'''If you attempt to create an object for this class, it won't work'''

# Child classes
class Car(Vehicle):
  # complete the methods on the parent abstract class by making the non abstract
  def go(self):
    print('You drive the car')
  def stop(self):
    print("You stop the car")

class Bike(Vehicle):
  # complete the methods on the parent abstract class by making the non abstract
  def go(self):
    print('You drive the bike')
  def stop(self):
    print("You stop the bike")


## Using child objects to run the methods
Car().go()
Car().stop()

Bike().go()
Bike().stop()

'''Note: each children must contain all the methods that were abstract in the parent class, else, it won't run
So, if a parent has 2 abstract methods, those 2 should be present on each child'''