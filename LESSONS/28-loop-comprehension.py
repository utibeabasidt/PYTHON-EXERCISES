'''This is a simpler way to loop through a value
Syntax:
  loop_variable = [statment for i in range if condition (optional)]
'''

# Code to print numbers from 1 to 10
nums = [i for i in range(11)]
print(nums) # prints in a list

# Printing even numbers from 2 to 20
even_nums = [i for i in range(1, 21) if i % 2 == 0]
print(even_nums)