my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list) # prints the entire list
print(my_list[0]) # prints the value in the list
print(my_list[0:3]) # prints the first three values in the list
print(my_list[0:7:2]) # prints the first seven values, but increment by 2
my_list[9] = 0 # change value from 10 to 0

# looping through the list
for number in my_list:
  print(number, end=' ')

print(len(my_list)) # returns the number of values in a list
print(2 in my_list) # returns whether true or false a value is in a list
print(3 not in my_list) # returns whether true or false a value is not in a list
