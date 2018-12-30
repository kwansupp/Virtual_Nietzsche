from collections import Counter
import pandas as pd
import os

test_sentence = []

for file in os.listdir('datasets'):
    #print(file)
    with open('./datasets/'+ file, 'r') as myfile:
        for line in myfile:
            for word in line.split():
               test_sentence.append(word)

trigrams = [(test_sentence[i], test_sentence[i + 1], test_sentence[i + 2])
            for i in range(len(test_sentence) - 2)]

bigrams = [(test_sentence[i], test_sentence[i + 1])
            for i in range(len(test_sentence) - 1)]

unigrams = [(test_sentence[i])
            for i in range(len(test_sentence))]

#print(trigrams[:3])

#print(len(trigrams))

#Count how often trigram occurs

grams_df = [pd.DataFrame({'gram':unigrams}), pd.DataFrame({'gram':bigrams}), pd.DataFrame({'gram':trigrams})]

grams_freq = [pd.DataFrame(columns=['grams','frequency']),pd.DataFrame(columns=['grams','frequency']),pd.DataFrame(columns=['grams','frequency'])]

idx = 0
for i in grams_freq:
    i['grams'] = grams_df[idx].gram.value_counts().keys().tolist()
    i['frequency'] = grams_df[idx].gram.value_counts().tolist()
    idx += 1
    print(i)

#TODO function that returns all the trigrams starting with given two words
def returnMostProbableWord(df, word1, word2):
    print(df[df['trigrams'].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)]['trigrams'].iloc[0][2])

returnMostProbableWord(trigram_freq, "Thus", "spake")

#print(trigram_counts[trigram_counts["col"].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)])
