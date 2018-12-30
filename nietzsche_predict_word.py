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
    lambda1 = 0.05
    lambda2 = 0.40
    lambda3 = 0.55
    flag2words = (len(wordlist)==2)
    print(flag2words)
    print(wordlist[0])
    #print(df[0])

    highscore = ('NaN', 0)

    for index, row in df[0].iterrows():
        freq_uni = row['frequency']
        checkedBi = False
        checkedTri = False
        for index1, row1 in df[1][df[1]['grams'].apply(lambda x: True if wordlist[0]==x[0] and row['grams']==x[1] else False)].iterrows():
            freq_bi = row1['frequency']
            checkedBi = True
            for index2, row2 in df[2][df[2]['grams'].apply(lambda x: True if wordlist[0]==x[1] and wordlist[1]==x[0] and row['grams']==x[2] else False)].iterrows():
                freq_tri = row2['frequency']
                checkedTri = True
        if (not checkedBi):
            freq_bi = 0
            freq_tri = 0
        elif(not checkedTri):
            freq_tri = 0
        probability = lambda1*freq_uni+lambda2*freq_bi+lambda3*freq_tri
        if (probability > highscore[1]):
            highscore = (row['grams'],probability)
            print(highscore)
        #print(highscore)
    return highscore



    #df[0][df[0]['grams'].apply(lambda x: True if wordlist[0]==x else False)]
    #print(freq_uni)

    #for index, row in df[0].iterrows():
#        for index, row in df[1][df[1].apply(lambda x: True if row['grams'] in x[0] else False)].iterrows():
#            for index, row in df[2][df[2].apply(lambda x: True if row['grams'][0] in x[0] and row['grams'][1] else False)].iterrows():
#                print(row['grams'])

    #    print(row['c1'], row['c2'])
    #print(df[df['trigrams'].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)]['trigrams'].iloc[0][2])

print(wordGenerator(grams_freq, ["spake","Thus"]))

#print(trigram_counts[trigram_counts["col"].apply(lambda x: True if "This" in x[0] and "is" in x[1] else False)])
