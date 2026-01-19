'''TRY-CATCH is used to handle exception (errors that makes a code to stop running)'''

## A PROGRAM TO CATCH THE EXECPTION WHEN A USER INPUTS A STRING INSTEAD OF AN INTEGER
try:
  number = int(input('Enter number: '))
  print('Correct.', number)
except ValueError:
  print("Wrong input")

## A PROGRAM TO CATCH THE EXCETION WHEN A USER REQUEST FOR AN INDEX THAT ISN'T IN AN ARRAY
try:
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  choice = int(input('Enter the index you\'ll want to find: '))
  print(my_list[choice])
except IndexError: # checking if index is under the range in the list
  print('list index out of range')
except ValueError: # checking for correct data input
  print('Only accepts whole numbers')
except: # checking if there is any other problem that is unknowm
  print('Something went wrong.')


'''You could also try for nested try-except methods'''

### ELSE IN TRY-EXCEPT (Runs only when the try function runs and vice versa)
## A PROGRAM TO CATCH THE EXECPTION WHEN A USER INPUTS A STRING INSTEAD OF AN INTEGER AND TELL IF IT WAS SUCCESSFUL OR NOT
try:
  number = int(input('Enter number: '))
  print(number)
except ValueError:
  print("Wrong input")
else:
  print('Correct input')

### FINALLY IN TRY-EXCEPT (runs when the try function runs or not)
## A PROGRAM TO CATCH THE EXECPTION WHEN A USER INPUTS A STRING INSTEAD OF AN INTEGER AND TELL IF IT WAS SUCCESSFUL OR NOT, BUT STILL TELLS THE USER THAT THE CODE RAN
try:
  number = int(input('Enter number: '))
  print(number)
except ValueError:
  print("Wrong input")
else:
  print('Correct input')
finally:
  print('Code succefully ran')
