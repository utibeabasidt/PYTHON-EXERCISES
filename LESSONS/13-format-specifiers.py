x = 300000
print(f'{x:.2f}') # returns the number with 2 decimal points
print(f'{x:10}') # returns the number with 10 spacings, including it
print(f'{x:010}') # returns the number with 10 spacings, including it, but fill every empty space with 0
'''You could make use of > (right alignment), < (left alignment), and ^ (center alignment)'''
print(f'{x:+}') # returns a positive number a positive sign at the beginning
print(f'{x: }') # retuns a space to any positive number
print(f'{x:,}') # returns a comma to every thousand