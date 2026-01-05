countries = ['Nigeria', 'USA', 'Cameroon', 'UK', 'Ghana', 'Australia']
fruits = ['Mango', 'Grape', 'Guava', 'Cucumber']
numbers = list((1, 2, 3, 4, 5)) # note: double brackets

print(countries) # whole list
print(fruits) # whole list
print(numbers) # whole list

# INDEXING
print(countries[4]) # Ghana (single indexing) 
print(fruits[0][4]) # o (2d indexing)
print(countries[1::]) # from index 1 till the end
print(fruits[0:4:2]) # using start, stop, and step method
print(type(countries)) # <class 'list'> 
# Negative Indexing
print(countries[-1]) # Australia
print(countries[-3:-1]) # Uk and Ghana

# Changing a value in the list
fruits[0] = 'Apple' # from mango to apple
print(fruits) 

# SOME FUNCTIONS
print(len(countries)) # 6