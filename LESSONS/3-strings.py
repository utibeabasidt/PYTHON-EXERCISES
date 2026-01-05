number = '123456789'
# INDEXING
print(number[1]) # 2
print(number[0:3]) # 123
print(number[0:8:2]) # start = 0, end (exclusive) = 8, step = 2 => 1357
print(number[0:]) # 123456789
print(number[0::2]) # 13579
print(number[-1]) # 9
print(number[-4:-1]) # 678
print(number[-8:]) # 23456789
print(number[-8::2]) # 2468

# Note: Why start with -1 in counting from the back is because of the number line, and 0 is neither a positive nor a negative number

name = 'Utibe'
# OTHER STRING FUNCTIONS
print(name.upper()) # UTIBE
print(name.lower()) # utibe
print(name.islower()) # false, because of the initial varaible
print(name.isupper()) # false, because of the initial varaible
print(name.lower().islower()) # true, because the characters are all lowercase
print(name.capitalize()) # Utibe
print(len(name)) # 5
print(name.index('e')) # this checks the the index of the first recurring character => 4
print(name.replace('e', 'y')) # Utiby
print(name.isdigit()) # false
print(name.find('i')) # 2
print(name.rindex('e')) # this one checks the index of the last recurring character => 4
