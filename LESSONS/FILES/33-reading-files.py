# Get the file path
countries_file_path = 'LESSONS/FILES/countries.txt'

# Open the file and save it in a variable
countries = open(countries_file_path, 'r')

# You can check if it is readable (Optional)
print(countries.readable())

# You can read the first paragraph of your file (you can do it subsequently to get other paragraph)
print(countries.readline()) 

# You can read all the contents in the file
print(countries.read())

# You can read all the contents but in a list, giving room for looping and indexing
print(countries.readlines()) # prints in a list
'''It is advisable you only use this method when the other two methods are not used'''

# Close the file
countries.close()