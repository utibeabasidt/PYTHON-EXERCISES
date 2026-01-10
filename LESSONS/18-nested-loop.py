my_list = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  ['*', 0, '#']
]

# SINGULAR LOOPING
for each_row in my_list:
  print(each_row)

# NESTED LOOPING
for each_row in my_list:
  for each_value in each_row:
    print(each_value, end=" ")
  print('')
  ## format: 
  '''
  1 2 3
  4 5 6
  7 8 9
  * 0 #
  '''
