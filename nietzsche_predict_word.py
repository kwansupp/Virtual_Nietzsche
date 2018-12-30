from collections import Counter
import pandas as pd
import os

test_sentence = []

"""
for file in os.listdir('datasets'):
    #print(file)
    with open('./datasets/'+ file, 'r') as myfile:
        for line in myfile:
            for word in line.split():
               test_sentence.append(word)
"""

with open('clean_data.txt', 'r') as myfile:
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
def wordGenerator(df, wordlist):
    flag2words = (len(wordlist)==2)
    #print(flag2words)
    #print(wordlist[0])
    #print(df[0])

    freq_uni = df[0][df[0]['grams'].apply(lambda x: True if wordlist[0]==x else False)['frequency']


    #for index, row in df[0].iterrows():
#        for index, row in df[1][df[1].apply(lambda x: True if row['grams'] in x[0] else False)].iterrows():
#            for index, row in df[2][df[2].apply(lambda x: True if row['grams'][0] in x[0] and row['grams'][1] else False)].iterrows():
#                print(row['grams'])

    #    print(row['c1'], row['c2'])
    #print(df[df['trigrams'].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)]['trigrams'].iloc[0][2])

#wordGenerator(grams_freq, ["for", "spake"])

#print(trigram_counts[trigram_counts["col"].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)])
