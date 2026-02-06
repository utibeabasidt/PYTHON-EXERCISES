'''This is when a inner function can have access to the variables in the outer function after the parent function has returned '''

def outer_function(name):
  coins = 3
  def inner_function():
    nonlocal coins # way to modify a variable that is not local
    if coins > 1:
      print(f'{name} has {coins} coins left.')
    if coins == 1:
      print(f'{name} has {coins} coin left.')
    elif coins == 0:
      print(f'{name} is out of coins.')
    coins -= 1
  return inner_function # once we call the parent function, return the value you get from the inner function

utibe = outer_function('utibe') # fulfilling the logic of the outer function (returning a value)
# fulfilling the logic of the inner function (printing a value)
utibe()
utibe()
utibe()
utibe()
''' because we are calling a return (outer) function that is calling a void (inner) function '''