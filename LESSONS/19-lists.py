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
my_list.append(11) # this adds a new value to the list
my_list.remove(11) # this removes a value from the list
my_list.insert(10, 11) # this checks for the index and puts in a value there. if there were other values after it, their index would change
my_list.sort() # this arranges the values in alphabetical and numerical order. note, if you want to reverse in order, you need to sort first
print(my_list.index(5)) # this returns the index that belongs to the value
print(my_list.count(5)) # this counts the number of times a value has occured in a list
my_list.clear() # this clears all the values in the list, making it empty
del my_list # this deletes the container permanently