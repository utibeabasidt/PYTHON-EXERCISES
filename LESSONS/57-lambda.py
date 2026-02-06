'''This is a single expression that returns a value. This is more or less a ternary/anonimous function'''

# def func_name():
#   print expression

# Not using param
name = lambda : print('Utibe')
name()

# Using param
number = lambda num : print(num)
number(2)

# Using more than one param
add_two_values = lambda a, b, c : print(a + b * c)
add_two_values(5, 5, 40)

# Using return value
add_two = lambda num : num + 2 # return num + 2
print(add_two(4))


# Applications in closures
def outer_function(name):
  return lambda : name
name = outer_function('Utibeabasi') 
print(name())
'''The code above is a way of calling a retun function that has a return function inside it. The inner function is a lambda function that is returning the value of the name variable in the outer function. The outer function is returning the inner function, and we are calling the outer function to get the inner function, and then calling the inner function to get the value of name.'''

def out_function(name):
  result = lambda : print(name)
  result()
out_function('Python') # fulfilling the logic of the outer function (printing a value)

