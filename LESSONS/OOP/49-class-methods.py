'''These are methods that allows operations related to the class itself (cls) instead of (self). it uses class varaibles (data)'''

class Student():
  # class variable
  count = 0 
  total_gpa = 0

  # Instance methods
  def __init__(self, name, gpa):
    # instance variable
    self.name = name
    self.gpa = gpa

    Student.count += 1
    Student.total_gpa += self.gpa

  def get_info(self):
    print(f'{self.name} {self.gpa}')

  # Class method
  @classmethod
  def get_count(cls):
    print('Total number of students added =', cls.count)
    if cls.count == 0:
      print('The average gpa for all students course =', cls.count)
    else:
      print(f'The average gpa for all {cls.count} students course = {cls.total_gpa/cls.count:.2f}')

student1 = Student('Utibe', 4.5)
student2 = Student('Utibe', 4.6)
student2 = Student('Utibe', 4.4)
student2 = Student('Utibe', 4.2)
student2 = Student('Utibe', 4.8)
student2 = Student('Utibe', 4.71)
student2 = Student('Utibe', 4.77)
student2 = Student('Utibe', 5.0)

student2.get_info() # instance method

# Class methods
Student.get_count() # runs without creating the object because it works in the class