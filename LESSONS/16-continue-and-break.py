'''CONTINUE: It skips an iteration once a condition is true
BREAK: It stops the loop once the condition is true
Note: Codes that are under in the scope where continue and break are in will not run'''

## CONTINUE
# if a number is odd, skip it and print the next one which is even
for i in range(1, 21):
  if i % 2 != 0:
    continue
    print('end') # will not run
  print(i)

## BREAK
# while counting, print the numbers, but once it reaches 10, stop counting
for i in range(1, 21):
  print(i)
  if i == 10:
    break
    print('end') # will not run