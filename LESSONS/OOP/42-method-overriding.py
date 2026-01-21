'''This means that the method of the child class will override the method of the parent class if they have the same method name'''

class Parent:
  def greet(self):
    print("hello")

class Child(Parent):
  def greet(self):
    print('Hello world')

Child().greet() 