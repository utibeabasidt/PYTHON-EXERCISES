import module1 as m1

print(m1.name) # importing a variable
m1.greet_name(m1.name) # importing a function

for num in m1.my_list:
  print(num)

print(__name__) # the result would be __main__, because you are running it in its own file
print(m1.__name__) # the result would be module1, because you are running module1 in another file