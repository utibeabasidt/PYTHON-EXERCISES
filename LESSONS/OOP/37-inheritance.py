'''Animal is the parent class'''

class Animal:
  # Constructor
  def __init__(self, name):
    self.name = name
  # Methods
  def eat(self):
    print(f'{self.name} is eating')
  def move(self):
    print(f'{self.name} is moving')


'''Child classes'''
class Dog(Animal):
  def speak(self):
    print(f'{self.name} barks')

class Mouse(Animal):
  def speak(self):
    print(f'{self.name} squeek')

class Cat(Animal):
  def speak(self):
    print(f'{self.name} meows')

dog1 = Dog('Dog1')
mouse1 = Mouse('Mouse1')
cat1 = Cat('Cat1')

# using it's own attribute
print('Own Attributes')
dog1.speak() 
mouse1.speak() 
cat1.speak() 

# inheriting attributes from the parent
print('\nInherent Attributes')
dog1.eat() 
mouse1.eat() 
cat1.eat() 

'''Don't worry about the self object and hassle of creating constructors, the child classes would inherit the constructors and instance variables from the parent class'''