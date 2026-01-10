my_dict = {
  'name': 'Utibe',
  'age': 19,
  'status': 'Relationship',
  'nationality': 'Nigerian',
  'gender': 'Male',
  'friends': ['Utibe', 'Godswill', 'Kelvin']
}

print(my_dict['age']) # This gets the value assigned to that particular key
print(my_dict.get('age')) # This also gets the value assigned to that particular key
print(len(my_dict)) # This gets the number of key-value pairs in that dictionary
print(my_dict.__len__()) # This also gets the number of key-value pairs in that dictionary
print(my_dict.keys()) # This gives all the keys in a list
print(my_dict.values()) # This gives all the values in a list
print(my_dict.items()) # This gives all the keys and values in respected pairs

## How to print the key and value together using a loop method (study loops first before trying this out)
for key, value in my_dict.items():
  print(f'Key: {key}\tValue: {value}')