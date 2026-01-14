my_set = {0, 1, 2, 3, 4, 5}

print(my_set) # this prints the entire set
print(len(my_set)) # this prints the total number of values in a set
print(2 in my_set) # this returns true or false to whether there is a value in a set
print(8 not in my_set) # this return true or false to whethere there isn't a value in a set
my_set.add(6) # this adds a value to the end of the set. note that it doesn't allow duplicate of values
my_set.remove(6) # this is removes a value from the set
my_set.pop() # this removes the first value in the set
my_set.clear() # this clears all the contents in the set (container)
del my_set # this permanently deletes the set itself