'''A 2d collection is a colection made up of one or more collections. It's mostyle used in developing a matrix of data
You can do it for lists, set, and tuples
You can use different collections, but the inner collections all need to be the same'''

my_2d_collection = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]

print(my_2d_collection[0]) # prints the first row
print(my_2d_collection[0][1]) # prints the 2nd value in the first row

# Looping through a 2d collection
for row in my_2d_collection:
  print(row)
  for each_value in row:
    print(each_value, end=" ")
  print(' ')