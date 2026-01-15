'''Also known as SWITCH-CASE in other programming languages. It is an alternative to using many else-ifs statements'''

day = input('Enter a day in the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ').capitalize()
match day:
  case 'Monday':
    print('It is Monday')
  case 'Tuesday':
    print('It is Tuesday')
  case 'Wednesday':
    print('It is Wednesday')
  case 'Thursday':
    print('It is Thursday')
  case 'Friday':
    print('It is Friday')
  case 'Saturday':
    print('It is Saturday')
  case 'Sunday':
    print('It is Sunday')
  case _: # this acts as an else statement
    print('Invalid input.')

'''You can also use OR logical operator too'''
value = int(input('Enter a number that is 4 or 2: '))
match value:
  case 4 | 2:
    print('Correct!')
  case _:
    print('incorrect value')