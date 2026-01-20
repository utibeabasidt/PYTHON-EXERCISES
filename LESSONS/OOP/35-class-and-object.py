'''An object is a bundle of related attributes (variables) and methods (functions). A method is a kind of function that runs with an object.
E.g of objects: Book, Cup, Phone, etc.
A class is a sructure for creating one or more objects'''

# Classes in OOP
class Car:
  # initialising the constructor
  def __init__(self, model, year, price, color, for_sale):
    # getting the parameters and saving it to the object attribute, self
    self.model = model
    self.year = year
    self.price = price
    self.color = color
    self.for_sale = for_sale

    # You can also use the print statement inside when you want to access all the objects and attributes
    car_details = f'The car model is {self.model}. The year is {self.year}. The price is ${self.price}. The car color is {self.color}.'
    sales_report = 'The car is for sale' if self.for_sale == True else 'The car is not for sale.'

    print(car_details, sales_report)
  
  # Methods in OOP
  def drive(self):
    print(self.model,'is driving') # you can access the attributes using the self parameter


# Objects in OOP
car1 = Car("Benz", 2026, '30,000', 'blue', True)
car2 = Car('Mustang', 2026, '25,000', 'Red', False)

# You can also use the print statement outside when you want to access a particular object and attribute
print(car1.model)
print(car2.model)

# You need to call the method for each objects even when the self parameter is initialized
car1.drive() # Benz is driving
car2.drive() # Mustang is driving