# start of function
def greeting_function() :
  print('Hello')
# close of function
greeting_function()

# PARAMETERS
def print_list(lists):
  print(lists)
list1 = [1, 2, 3, 4]
print_list(list1)

def message(name, age, colour, lecture="Python Class"):
  print(f"Hello {name}. You are {age} years old. Your favourite color is {colour}. You are attending {lecture}")
name = input('Enter your name: ')
age = int(input("Enter your age: "))
colour = input("Enter your favorite color: ")
message(name, age, colour)

# how to print one particular argument even when there are numerous arguments to one parameter:
def hi(*names):
  print('Hello', names[0])
hi('John', 'Mike', 'Raph')