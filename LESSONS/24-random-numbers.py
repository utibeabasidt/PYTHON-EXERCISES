'''To generate random numbers, you must first of all import the random module'''

import random as r

print(r.randint(1, 100)) # this prints a random integer between 1 and 100, no exclusivity
print(r.random()) # this prints a random float between 0 and 1
print(r.choice([1, 2, 3, 4, 5])) # this print any number in the list randomly

# How to shuffle a list:
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r.shuffle(number)
print(number)