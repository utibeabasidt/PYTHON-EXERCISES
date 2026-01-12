name = 'Utibe'

print(len(name)) # prints the number of characters in a string
print(name.find('i')) # returns the index of the first occurance of that character
print(name.index('i')) # returns the index of the first occurance of that character
print(name.rfind('i')) # returns of the index of the last occurance of that character
print(name.capitalize()) # Capitalises the first letter in the string
print(name.upper()) # returns the uppercase of the string
print(name.lower()) # returns the lowercase of the string
print(name.isdigit()) # returns true or false if the string ONLY contains digits
print(name.isalpha()) # returns true or false if the string ONLY contains alphabets
print(name.islower()) # returns true or false if the string ONLY contains lowercases
print(name.isupper()) # returns true or false if the string ONLY contains uppercases
print(name.isspace()) # returns true or false if a string contains ONLY spaces (no character, but spaces)
print(name.count('i')) # returns the numner of times a character has occured in a string
print(name.replace('e', 'y')) # replaces the former with the latter
'''Note: replace() replaces all and each of the liked characters that are in the string with the second letter
e.g:
Utibeeeee = Utibyyyyy
'''
print(name.__add__('e')) # this appends a value to the end of the string
print(name.__contains__('e')) # this checks if the string contains a character
print(name.startswith('U')) # returns true or false if a string starts with a particular character
print(name.endswith('')) # returns true or fale if a string starts with a particular character