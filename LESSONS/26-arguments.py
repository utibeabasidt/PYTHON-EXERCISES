# DEFAULT ARGUMENTS
def get_tithe(income, tithe_percent = 0.1):
  return income * tithe_percent
print(get_tithe(5000))
print(get_tithe(500, 0.5)) # you can still override the default argument

# KEYWORD ARGUMENT (note, the order to postitioning arguments doesn't matter)
def personalised_greeting(greeting, title, first_name, last_name):
  print(f'{greeting}, {title} {first_name} {last_name}.')
personalised_greeting(first_name='Utibe', last_name='Thompson', title='Mr.', greeting='Good Afternoon')
'''end=' ' and sep='-' are examples of keyword arguments too'''

## ARBITUARY (VARYING) ARGUMENTS
# *args -- accepts multiple normal arguments and save it in a tuple
def print_total(*numbers):
  total = 0
  print(numbers) # prints them in tuples
  for each_number in numbers:
    total += each_number
  return f'The total of all the numbers is {total}'
print(print_total(1, 2, 3, 4, 5))

# kwargs -- accepts key word arguments alone and saves them in a dict (key and value)
def get_users(**id_and_value):
  for key, value in id_and_value.items(): # with kwargs, you can access methods in dictionary
    print(f'{key}: {value}')
get_users(a='Utibe', b='David', c='Thompson')

'''Note: You can use both args and kwargs inside one function, just know that kwargs would have to be keyworded and just know how to be creative'''