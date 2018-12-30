from collections import Counter
import pandas as pd

test_sentence = []

with open('test_nietzsche.txt', 'r') as myfile:
    for line in myfile:
        for word in line.split():
           test_sentence.append(word)

print(test_sentence)

trigrams = [(test_sentence[i], test_sentence[i + 1], test_sentence[i + 2])
            for i in range(len(test_sentence) - 2)]

print(trigrams[:3])

print(len(trigrams))

#TODO: count how often trigram occurs
#myset = unique(tigrams)
#print(myset)

df = pd.DataFrame({'col':trigrams})
print(df)
print(df.col.unique())

#counts = Counter(test_sentence)
#print(counts)
print(df.col.value_counts())
