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

#print(trigrams[:3])

#print(len(trigrams))

#Count how often trigram occurs

trigrams_df = pd.DataFrame({'trigram':trigrams})
#print(df)
#print(df.col.unique())
#print(df.col.value_counts())

val_col = trigrams_df.trigram.value_counts().keys().tolist()
freq_col = trigrams_df.trigram.value_counts().tolist()

trigram_freq = pd.DataFrame(columns=['trigrams','frequency'])
trigram_freq['trigrams'] = val_col
trigram_freq['frequency'] = freq_col
#print(trigram_freq)

#TODO function that returns all the trigrams starting with given two words
def returnMostProbableWord(df, word1, word2):
    print(df[df['trigrams'].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)]['trigrams'].iloc[0][2])

returnMostProbableWord(trigram_freq, "Thus", "spake")

#print(trigram_counts[trigram_counts["col"].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)])
