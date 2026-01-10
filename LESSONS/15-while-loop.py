## A WHILE LOOP TO KEEPING PROMPTING A USER TO USE A PASSWORD OF 6 OR MORE CHARACTERS
password = input('Enter a password of 6 characters and more: ')

while len(password) < 6:
  print('Password should be 6 characters or more.')
  password = input('Enter again: ')

print('Login Successful. Welcome.')

## LOOPING SYSTEM TO CHECK IF A USER INPUTS A NUMBER MORE THAN 10, AND IF HE A ATTEMPTS 5 TIMES, THEN THE CODE SHOULD STOP RUNNING

number = int(input('Enter a number greater than 10: '))
number_of_attempts = 1

# While the number is less or equal to ten and the number of attempts is less than 5, and if they're both true, then still run the code
while number <= 10 and number_of_attempts < 5:
  number = int(input('Number should be greater than 10. Enter again: '))
  number_of_attempts += 1

# If the while loop is broken, check if the number is greater than 10 or check if the number of attempts has reached 5 at least
if number > 10:
  print("Good")
elif number_of_attempts == 5:
  print('Timeout')