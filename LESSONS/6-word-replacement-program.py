sentence = input('Enter a sentence: ').lower() # get the sentence

print(f'your sentence is: {sentence.capitalize()}') # print the initial sentence

word1 = input('What word would you like to replace: ') # ask for the word to be replaced

word2 = input(f'what word would you like to replace "{word1}" with: ') # ask for the substitute

sentence = sentence.replace(word1, word2) # replace all recurring word1 with word2
print(sentence.capitalize()) # print new sentence