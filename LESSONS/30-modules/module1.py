name = 'Utibe'
my_list = [1, 2, 3, 4, 5]

def greet_name(name):
  print('Hello ' + name)

print(__name__) # the result would be __main__, because you are running it in its own file

def main():
  print('Hello world')

# function to check if we are actually running the file directly
if __name__ == '__main__':
  main()
