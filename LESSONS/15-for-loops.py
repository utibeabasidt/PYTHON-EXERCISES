'''This loop executes a block of code under a fixed number of times
  Syntax:
    for i in range(start, end(exclusive), step): => when you are iterating over a range of number
                                      OR
    for temp_variable in variable: => when you are iterating over a sequence
'''

## PRINTING NUMBERS FROM 1 TO 20
for i in range(1, 21):
  print(i)

## PRINTING EACH CHAR IN A STRING
name = 'utibe'
for each_letter in name:
  print(each_letter)

## REVERSED RANGE
for each_letter in reversed(name):
  print(each_letter)

## ITERATING OVER A STEP
# Printing even numbers from one to 20
for number in range(1, 21, 2):
  print(number + 1) # 2, 4, 6...

## REVERSING USING A STEP
# Printing from 20 to 1
for i in range(20, 0, -1):
  print(i)