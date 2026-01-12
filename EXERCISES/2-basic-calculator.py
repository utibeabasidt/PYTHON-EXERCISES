'''first_input = input('Enter first number: ')
operator = input('Enter an operator (+, -, *, /): ')
second_input = input('Enter second number: ')

calculation = first_input + operator + second_input

print(f"The result is {eval(calculation)}") '''

first_input = int(input('Enter first number: '))
operator = input('Enter an operator (+, -, *, /): ')
second_input = int(input('Enter second number: '))
calculation = 0

if operator == '+':
  calculation = first_input + second_input
  print(f"The result is {calculation}")
elif operator == '-':
  calculation = first_input - second_input
  print(f"The result is {calculation}")
elif operator == '*':
  calculation = first_input * second_input
  print(f"The result is {calculation}")
elif operator == '-':
  calculation = first_input - second_input
  print(f"The result is {calculation}")
elif operator == '/':
  calculation = first_input / second_input
  print(f"The result is {calculation}")
else:
  print('Wrong Input. Try again')
  
