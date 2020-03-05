import numpy as np

# Churchill's speech
churchill = open('churchill.txt').read()
keywords = churchill.split()
print(keywords)

# Make state chart for follow-up words
keylist = []
for i in range(len(keywords)-1):
    keylist.append( (keywords[i], keywords[i+1]))
print(keylist)

# Create key-value pairs based on follow-up words
word_dict = {}
for beginning, following in keylist:
    if beginning in word_dict.keys():
        word_dict[beginning].append(following)
    else:
        word_dict[beginning] = [following]
print(word_dict)

# Generate the first word and append to a list
first_word = np.random.choice(keywords)
while first_word.islower():
    first_word = np.random.choice(keywords)
word_chain = [first_word]

# Append new words based on Markov model to a list
WORDCOUNT = 40
for i in range(WORDCOUNT):
    word_chain.append(np.random.choice(word_dict[word_chain[-1]]))

# Form a sentence from the list of words
sentence = ' '.join(word_chain)
print(sentence)
