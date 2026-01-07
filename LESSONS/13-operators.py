# ARITHMETIC OPERATORS
print(2+2) # Addition
print(2-2) # Subtraction
print(2*2) # Multiplication
print(2/2) # Division
print(3//2) # Floor Division (ignore any decimal and give me the whole number alone)
print(3%2) # Modulus
print(3**2) # Exponentiation

x = 5
y = 3

# OTHER ARITHMETIC OPERATORS
x+=y # Add the value of y to x and store the result in x
print(x)
x-=y # Subtract the value of y from x and store the result in x
print(x)
x*=y # Multiply the value of x by y and store the result in x
print(x)
x/=y # Divide the value of x by y and store the result in x
print(x)

# COMPARISON OPERATORS
print(x==y) # False
print(x!=y) # True
print(x>y) # True
print(x>=y) # True
print(x<y) # False
print(x<=y) # False

# BITWISE OPERATORS
print(x and y) # If the LHS is truthy value, then the RHS is printed, if the LHS is false, then all are false
print(x or y) # If the LHS is a truthy value, then the LHS is printed. if the LHS is false, then the RHS is printed

name = 'Utibe'

# MEMBERSHIP OPERATORS
print('i' in name) # True
print('i' not in name) # False

a = 1
b = 1

# IDENTITY OPERATORS
print(a is b) # True
print(a is not b) # False