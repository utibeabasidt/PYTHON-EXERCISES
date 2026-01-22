'''Here, the composed object directly own its components, which cannot exist independently(on its own). It uses an 'owns-a' relationship(buying).
Here, you cannot create an object outside of a class if and only if the object has already been created inside another class'''

class Engine:
  def __init__(self, horse_power):
    self.horse_power = horse_power

class Wheel:
  def __init__(self, wheel_size):
    self.wheel_size = wheel_size

class Car:
  def __init__(self, model, horse_power, wheel_size):
    self.model = model
    # creating the objects inside this class so that it won't be created again outside (A method of owning)
    self.engine = Engine(horse_power) # owns the engine
    self.wheel = Wheel(wheel_size) # owns the wheel
  def car_details(self):
    # Acessing the instant variables saved in the Engine/Wheel constructor that is then saved in the Car constructor
    print(f'A {self.engine.horse_power} HP {self.model} with {self.wheel.wheel_size} Wheel size')

car = Car('Benz', 500, 30)
car.car_details()

'''Hint: Only assign parameters to your little composed classes. Don't do anything with them e.g we did not apply any methods or any action in engine and wheel classes'''