numbers = [1, 2, 3, 4, 5]
fruits = ['banana', 'apples', 'mangoes', 'oranges', 'mangoes']

# LIST METHODS
numbers.append(fruits) # type: ignore # this adds a list to a list
print(numbers)
fruits.append('cherry') # this adds a value to the end of a particular list
print(fruits)
fruits.insert(0, 'guava') # this adds a value to the preferred index in the list, thereby pushing the rest
print(fruits)
fruits.remove('banana') # this removes the first occuring value from the list
print(fruits)
print(fruits.index('cherry')) # this gets the index of a value in a list
print(fruits.count('mangoes')) # this gets the number of occurances of a value, checking if there are any duplicates
fruits.sort() # this arranges the list in ascending order
print(fruits)
fruits.reverse()
print(fruits)
## how to duplicate/copy a list
fruits2 = fruits.copy()
print(fruits, 'copied list')
fruits.pop() # this deletes the last value from a list
print(fruits)
fruits.pop(0) # this deletes the value that has the index 0
print(fruits)


fruits.clear() # this clears off the entire values in the list, making it empty
print(fruits)
del fruits # this clears off the list itself, making it undefined
# print(fruits) (not defined)
