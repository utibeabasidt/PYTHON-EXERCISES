# IF STATEMENT
if (3>2):
  print("3 is greater than 2")

# IF...ELSE STATEMENT
if(3>2):
  print('3 is greater than 2')
else:
  print('3 is not greater than 2')

# IF...ELSE-IF STATEMENT
if(3>2):
  print('3 is greater than 2')
elif(2<3):
  print("2 is not greater than 3")

# IF...ELSE-IF...ELSE STATEMENT
if(3>2):
  print('3 is greater than 2')
elif(2<3):
  print("2 is not greater than 3")
else:
  print('None is correct')

### EXERCISES
## CHECKING IF A NUMBER IS DIVISIBLE BY 5
number = int(input('Enter a value: '))
if number % 5 == 0:
  print(f'{number} is divisible by 5')
else:
  print(f'{number} isn\'t divisible by 5')

## CHECKING IF THE LENGHT OF A SENTENCE IS LESS THAN 10 OR NOT
sentence = input('Enter a sentence: ')
if sentence.__len__() < 10:
  print('Sentence is less than 10')
elif len(sentence) > 10:
  print('Sentence is greater than 10')

## CHECKING IF A NUMBER IS EVEN OR ODD
num = int(input('Enter a number: '))
if num % 2 == 0:
  print(f'{num} is an even number')
else:
  print(f'{num} is an odd number')
