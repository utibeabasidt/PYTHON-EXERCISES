'''A while loop repeats a block of code while a condition remains true
Syntax:
  while condition is true:
    statements

  statements(if the condition is altered)
'''

## A WHILE LOOP THAT PROMPTS A USER TO ENTER A PASSWORD THAT IS 6 CHARACTER OR MORE

password = input('Enter a password that is 6 characters or more: ')

while password.__len__() < 6:
  password = input('Password is lesser than 6, Try again: ')

print('Password created succesfully')