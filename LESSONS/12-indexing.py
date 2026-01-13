'''Indexing helps to access elements of a sequence (String, list, tuple, set, dictionaries)
[index-start:index-end:index-step]'''

num = '08130911817'

print(num[0]) # returns the character that belongs to the first index
print(num[5]) # returns the character that belongs to the sixth index
print(num[0:4]) # returns the characters that belongs from the first index to the fifth exclusive index (that means the stop index is not included itself)
print(num[4:]) # returns all the characters that starts from the fifth index till the end
print(num[:4]) # returns all the characters that start from the beginning till the fifth exclusive index
print(num[-1]) # returns the last character in the string but in backwards indexing
print(num[::2]) # returns all the characters from the begining to the end, but increment by 2. Ths means it will be skipping a step by 1 after picking a particular character.

## SIMPLE HACK: HOW TO REVERSE A STRING
print(num[::-1])