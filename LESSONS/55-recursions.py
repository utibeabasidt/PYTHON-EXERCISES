'''This is when a function calls itself inside it. Most times, it is used to create a looping system.'''

# Function to keeping adding one to a number until that number is 10
def add_num(num):
  # if num is greater than 10, break the loop
  if num > 10:
    return
  # else, print the number, increase it by one, and run the function again with the incremented number
  else:
    print(num)
    num += 1
    add_num(num)

add_num(1)



# Function to print a name for five times
def print_name(name, lenght_of_print):
  if lenght_of_print > 5:
    return
  else:
    print(name)
    lenght_of_print += 1
    print_name(name, lenght_of_print)

lenght_of_print = 1
print_name('Utibe', lenght_of_print)