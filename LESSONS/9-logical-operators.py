print (3 and 4) # if the LHS is true, the result is the RHS
print(False and 4) # if the LHS is false, the result is its value
print(3 or 4) # if the LHS is true, the result will be the value
print(False or 4) # if the LHS is false, the result will be the RHS

age = 18
if age >= 18 and age <= 100:
  print('You are an adult and you won\'t die any soon')

# ALternative to write AND logical statement

if 18 <= age <= 100:
  print('You are an adult and you won\'t die any soon (Version 2)')


if age > 0 or age > 100:
  print('You maybe above 0 or greater than zero.')

if not age == False:
  print('Not having an age is false')