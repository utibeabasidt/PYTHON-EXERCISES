# Get the file path (You can create yours or you use an already existing one)
file_path = 'LESSONS/FILES/countries2.txt'

# Open the file and make it writable
countries_file = open(file_path, 'w')

# Check if the file is writable
print(countries_file.writable())

# You can write into the end of the file
countries_file.write('This a new line') 
'''this creates a file called 'countries2.txt', and then input this text here'''

# You can as well add another paragraph
countries_file.write('\nThis is another paragraph')

# Don't forget to close afterwards
countries_file.close()