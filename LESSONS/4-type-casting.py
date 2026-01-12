'''THIS IS BASICALLY COMVERTING A VARAIBLE FROM ONE DATATYPE TO ANOTHER'''

value = 1
print(type(value)) # prints the data type(int)
print(str(value)) # prints the string version of the value ('1')
print(int(value)) # prints the int version of the value (1)
print(float(value)) # prints the float version of the value (1.0)
print(bool(value)) # prints the boolean version of the value 

'''For strings, It is true if the string isn't empty.
This can be applies in if statements to see if a user input is empty or not'''
name = 'Utibe'
print(bool(name)) # True
name = ''
print(bool(name)) # False