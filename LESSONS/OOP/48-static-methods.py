'''A static method any method that belongs to a class rather than each object from that class. They are used when we don't want to create an object before using the methods. They are mainly used for general purposes that do not need constructors data. It uses its own parameter, rather than the self parameter.

Instance methods are methods that belong to each individual objects(Self) and they work in correspondence with that object. So, in order for you to use an instance method, you need to create an object'''

class Employee:
  # Instance Methods
  def __init__(self, employee_name, employee_position):
    self.employee_name = employee_name
    self.employee_position = employee_position

  def get_info(self): # for that object providing the parameters alone
    return (f'{self.employee_name}  {self.employee_position}')
  
  # Static methods
  @staticmethod # important to create
  def is_position_valid(employee_position):
    valid_position = ['Cook', 'Help', 'Manager']
    print(employee_position in valid_position)

employee1 = Employee('Utibe', 'CEO')
print(employee1.get_info()) # running the instance method (because it needs an object before running)

Employee.is_position_valid('Cook') # running the static method(without creating an object)