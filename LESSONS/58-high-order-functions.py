'''This is a function that takes one or more function as parameters'''

def call_hello_function(function1, function2):
  # calling the return functions
  print(function1())
  print(function2())

function1 = lambda : 'Hello world'
function2 = lambda : 'My name is Utibe'
call_hello_function(function1, function2) # fulfilling the outer function (calling two functions)