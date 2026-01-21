'''This allows a child class to inherit from one or more parent class'''

class Prey:
  def flee(self):
    print('This animal is fleeing')

class Predator:
  def hunt(self):
    print('This animal is hunting')

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass

Rabbit().flee() # Fleeing

Hawk().hunt() # Hunting

# Fleeing and Hunting
Fish().flee()
Fish().hunt()

'''Note: Those are shorthand ways for writing objects
i.e:  fish1 = Fish()
      fish1.flee()
      fish1.hunt()
'''