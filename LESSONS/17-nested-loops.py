'''This is a loop outside another loop'''

# Loop to print 1-10 in three places
for row in range(3):
  for number in range(1, 11):
    print(number, end=' ') # spacing each of the numbers
  print('') # breaking a new line after every row