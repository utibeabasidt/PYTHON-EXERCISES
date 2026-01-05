number1 = 78
number2 = 22
print(number1)
print(number2)

# ARITHMETIC OPERATIONS
print(number1 + number2) # Addition
print(number1 - number2) # Subtraction
print(number1 * number2) # Multiplication
print(number1 / number2) # Division
print(number1 % number2) # Modulus (Remainder)

# NUMBER FUNCTIONS
# Converting a number to a string
number3 = str(number1) 
print(type(number3)) # <class 'str'>
print(abs(-5)) # print the positve of a number no matter the state of it => 5
print(max(4, 2, 10, 16)) # print the highest number between two or more number
print(min(4, 2, 10, 16)) # print the low est number between two or more number
print(round(3.3)) # round to the nearest whole number
print(bin(3)) # getting the binary string of a whole number
print(pow(3, 2)) # finding the power of a whole number

# FUNCTIONS IMPORTED FROM MATH
from math import * # type: ignore
print(sqrt(3)) # prints the square root of a number as a float
print(floor(3.5)) # prints the lowest whole number => 3
print(ceil(3.3)) # prints the highest whole number => 4
print(sin(3)) # prints the sine of a number
print(cos(3)) # prints the cos of a number
print(tan(3)) # prints the tan of a number