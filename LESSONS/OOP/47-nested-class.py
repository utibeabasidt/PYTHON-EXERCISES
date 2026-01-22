'''This is a class defined within another class. We can logically group closely related classses. We can encapsulate private details that aren't relevant outside of the outer class. It also reduces the possibility of naming conflicts'''
'''Here, we can have two classes with the same name, as long as they're in different scopes'''

class Company:
  class Employee:
    # Constructor for the Employee
    def __init__(self, employee_name, employee_position):
      self.employee_name = employee_name
      self.employee_position = employee_position

    # Method to display each employee object
    def details(self, company_name):
      self.company_name = company_name
      return(f'This is {self.employee_name}, and he is the {self.employee_position} of {self.company_name}')

  # Constructor for the Company
  def __init__(self, company_name):
    self.company_name = company_name
    self.employees = []

  # Adding new sets of employees to the employee array
  def add_employee(self, employee_name, employee_position):
    new_employee = self.Employee(employee_name, employee_position) # using this constructor to get Object arguments
    self.employees.append(new_employee) # add each object (name and position)

  # Looping through to get the each objects
  def list_employee(self):
    print('LIST OF THE EMPLOYEES AND THEIR POSITIONS')
    for each_object in self.employees:
      print(each_object.employee_name, each_object.employee_position)

# Object Actions for Company Class
company1 = Company('GSP')
company1.add_employee('SAVIOUR', 'CEO')
company1.add_employee('ABAS', 'CFO')
company1.add_employee('UTIBE', 'CTO')
company1.list_employee()

print()

company2 = Company('Dhemiuz Hotels')
company2.add_employee('Idem', 'CEO')
company2.add_employee('Ukeme', 'CFO')
company2.add_employee('Dan', 'CTO')
company2.add_employee('David', 'Manager')
company2.list_employee()

print()

# Object actions for the Employee class (We may have little or no need to create these objects though)
employee1 = company1.Employee('Saviour', 'CEO')
print(employee1.details(company1.company_name))

print()

employee2 = company2.Employee('Idem', 'CEO')
print(employee2.details(company2.company_name))