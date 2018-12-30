"""
Rules for cleaning data.
1. remove all words with two or more consecutive uppercase letters
2. remove all numbers
#3. remove "preface", "prologue", "introduction", "foreword", "chapter"
"""

# import modules
import os
import re

# read files and extract lines for analysis
for file in os.listdir('datasets'):
	data_lines = []

	path = os.path.join('datasets', file)
	with open(path) as f:
		lines = f.readlines()
	data_lines.append(lines)

# remove line breaks
data_strings = [" ".join(d).replace("\n", "") for d in data_lines]

# separate sentences
data_sentences = []
for st in data_strings:
	st = re.sub("[^a-zA-Z0-9\.\?\! ]", "", st)
	st = re.sub("\d+\.", "", st)
	sentences = re.split("\. |\! |\?", st)
	data_sentences.append([[elem.lower() for elem in sent.split(" ") if elem != ""] for sent in sentences])
    
print(len(data_sentences[0]))

# recompile all sentences sentences into a file
output = open('clean_data.txt', 'w')

for i, st in enumerate(data_sentences[0]):
	sentence = ' '.join(st)
	# add begin and end tag for each sentence
	full = ' [BEGIN] ' + sentence + ' [END] '

	# write to file
	output.write(full)

output.close()
