## LOOPING THROUGH A STRING
for letter in 'Hello':
  print(letter) # print each letter seperatedly


## LOOPING THROUGH A LIST
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for each_number in my_list:
  print(each_number)

## LOOPING THROUGH A DICTIONARY
my_dict = {
  1: 'Utibe',
  2: 'Abasi',
  3: 'David',
  4: 'Thompson'
}
# looping through to get a tuple of each key and values together
for each_data in my_dict.items():
  print(each_data)

# looping through to get each key and value but not in tuples
for key, value in my_dict.items():
  print(f'{key} __ {value}')

# looping through to get each key alone
for each_key in my_dict.keys():
  print(each_key)

# looping through to get each value alone
for each_value in my_dict.values():
  print(each_value)


## LOOPING THROUGH A RANGE
for i in range(1, 11):
  print(i) # prints the index value from the index start (1) to the index explicit end (10)

name = 'Utibe'
for i in range(0, len(name)):
  print(name[i]) # prints each character through name indexing (0 to 4)

## DESIGNING A TRIANGLE
letter = '*'
for i in range(1, 11):
  # print the letter while iterating, and add an extra char to the letter
  print(letter) 
  letter += '*'

## BREAK
for i in range(1, 11):
  print(i)
  if (i == 5):
    break # if 5 is printed, stop the loop

## CONTINUE
for i in range (1, 11):
  if (i % 2 == 0):
    continue # if you see an even number, skip that particular iteration
  print(i)
else:
  print('Done')