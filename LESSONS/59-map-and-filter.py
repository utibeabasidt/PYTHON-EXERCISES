'''Map is a function in python used to apply a particular function to every item in an iterable'''

num = [1, 1, 3]
add_two = lambda x : x + 2 # function to return each number after 2 is added to it
new_num = map(add_two, num)
new_num = list(new_num) # after applying the function, save it into a new list
print(new_num)


'''Filter is a function in python used to select/filter values in an iterable based on a condition'''

num = [2, 3, 4]
find_even = lambda x : x % 2 == 0 # function to return all numbers that are even
num = filter(find_even, num)
num = list(num) # putting all the values in a list after filtering
print(num)
