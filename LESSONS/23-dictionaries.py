'''You can not duplicate keys, but you can duplicate values'''

my_dict = {
  1:  'Utibe',
  2:  'Samuel',
  3:  'David'
}

print(my_dict) # prints the entire dict
print(my_dict.keys()) # prints all the keys in the dist
print(my_dict.values()) # prints all the values in the dict
print(my_dict.items()) # prints all the key and value together in pairs in separate tuples
my_dict2 = my_dict.copy() # this copy all the contents to the later dict
print(my_dict.get(3)) # print the value that belongs to the key
my_dict.update({4:  'Favour'}) # this adds a value and a key, or updates a value in an already existing key-value pair
my_dict.pop(4) # this removes a pair related to the key
my_dict.popitem() # this removes the last key-value pair
my_dict.clear() # clears off the key-value pairs in the dict, making it empty
del my_dict