'''This allows a child class to inherit a parent class which inherits from another parent'''

## GRANDPARENT
class Animal:
  def __init__(self, name):
    self.name = name
  def intro(self):
    print(f'This is an animal. Its name is {self.name}.')

# PARENT
class Prey(Animal): # multilevel inheritance
  def flee(self):
    print(f'{self.name} is fleeing')

class Predator(Animal): # multilevel inheritance
  def hunt(self):
    print(f'{self.name} is hunting')

# CHILDREN
class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator): # multiple inheritance
  pass

rabbit = Rabbit('Rabbit')
hawk = Hawk('hawk')
fish = Fish('Fish')

rabbit.intro() # from grandparent
rabbit.flee() # Fleeing
print()

hawk.intro() # from grandparent
hawk.hunt() # Hunting
print()

fish.intro() # from grandparent
# Fleeing and Hunting
fish.flee()
fish.hunt()
print()