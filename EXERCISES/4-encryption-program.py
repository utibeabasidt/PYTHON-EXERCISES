'''ENCRYPTION PROGRAM'''

import random
import string

# Getting all the punctuation marks + numbers + lowercase alpohabets + uppercase alphabets in existence (we manually create a space variable)
characters = ' ' + string.punctuation + string.digits + string.ascii_letters
characters = list(characters) # turning all the individual characters to a list

# creating a key variable that has a copy of the characters
key = characters.copy() 
random.shuffle(key) # making a one time random such that each number in its index is different from the character in the same index

print(f'Chars: {characters}')
print(f'Key: {key}')

## ENCRYPTING
plain_text = input("Enter text you want to encrypt: ")
encrypted_text = ''

for each_letter in plain_text:
  index = characters.index(each_letter) # get the index of each letter from the list of the plain charaters
  encrypted_text += key[index] # concatenate the encrypted letters gotten from the same index  as the characters together (match-making)
  
print(encrypted_text)

## DECRYPTING
encrypted_text = input('Enter text you want to decrypt: ')
decrypted_text = ''
for each_encrypted_letter in encrypted_text:
  index = key.index(each_encrypted_letter) # look into the key list and fetch the index holding the letter
  decrypted_text += characters[index] # concatenate the decrypted letters gotten from the same index  as the key together (match-making)
  
print(decrypted_text)

