value = input('Enter a value: ')
calculation = value
is_running = True
is_response_invalid = True

while is_running: 
  operator = input('Enter an operator (+, -, *, /): ')
  # if the operator is valid, add it to the calculation
  if operator == '+' or operator == '-' or operator == '*' or operator == '/':
    calculation += f'{operator}' # add a space to each operator
    value = input('Enter another value: ')
    calculation += f' {value}' # add a space to each value
    response = input('Do you want to stop inputing values? (y/n): ')
    while is_response_invalid:
      # if the response is yes, then the response is valid and the calculation should stop
      if response.lower() == 'y':
        is_running = False
        is_response_invalid = False
      # if the response is no, then the response is valid but the calculation should keep running
      elif response.lower() == 'n':
        is_response_invalid = False
      # if the response isn't yes or no, then prompt the user again
      else:
        print('Wrong Response')
        response = input('Do you want to stop inputing values? (y/n): ')
  # if the operator isn't valid, display a wrong message and keep the calculation going, by asking the user to input it again
  else: 
    print('Wrong operator. Try again.')

print(f'The result of {calculation} is {eval(calculation)}')