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