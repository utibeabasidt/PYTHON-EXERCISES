import os # This module enables us to interact with the operating system

file_path = 'LESSONS/FILES/32-test.txt'

# Checking if the file exist
if os.path.exists(file_path):
  print("This file path exist")
else:
  print('This file path doesn\'t exist')

# Checking if the file is a folder or a file
if os.path.isfile(file_path):
  print('This is a file')
elif os.path.isdir(file_path):
  print('This is a folder')