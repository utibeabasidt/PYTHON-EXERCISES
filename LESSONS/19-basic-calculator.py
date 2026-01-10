first_input = input('Enter first number: ')
operator = input('Enter an operator (+, -, *, /): ')
second_input = input('Enter second number: ')

calculation = first_input + operator + second_input

print(f"The result is {eval(calculation)}")
