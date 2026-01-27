'''These are variables that are created outside the contructor and can be shared by objects'''

class Student:
  # Class Variables
  class_year = 2026 
  no_of_students = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.no_of_students += 1 # once you add a new student object, increase by one
    details = f'Name: {name} || Age: {age}'
    print(details)

student1 = Student('Utibe', 17)
student1 = Student('David', 74)
student1 = Student('Thompson', 20)

# Accessing the class variables
print(f'There are {Student.no_of_students} students that are graduating in the year of {Student.class_year}')
'''you can use objects to call the variables (student1.year, but for the sake of readability, access it by the class name'''