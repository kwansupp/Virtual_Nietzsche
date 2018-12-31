from collections import Counter
import pandas as pd
import os
import numpy as np

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

trigrams = [test_sentence[i]+" "+test_sentence[i + 1]+" "+test_sentence[i + 2]
            for i in range(len(test_sentence) - 2)]

bigrams = [test_sentence[i]+" "+test_sentence[i + 1]
            for i in range(len(test_sentence) - 1)]

unigrams = [test_sentence[i]
            for i in range(len(test_sentence))]

#print(trigrams[:3])

#print(len(trigrams))

#Count how often trigram occurs

grams_df = [pd.DataFrame({'gram':unigrams}), pd.DataFrame({'gram':bigrams}), pd.DataFrame({'gram':trigrams})]

grams_freq = [pd.DataFrame(columns=['grams','frequency']),pd.DataFrame(columns=['grams','frequency']),pd.DataFrame(columns=['grams','frequency'])]

idx = 0
for i in grams_freq:
    i['grams'] = grams_df[idx].gram.value_counts(normalize=True).keys().tolist()
    i['frequency'] = grams_df[idx].gram.value_counts(normalize=True).tolist()
    idx += 1

dict_bi = grams_freq[1].set_index('grams')['frequency'].to_dict()
dict_tri = grams_freq[2].set_index('grams')['frequency'].to_dict()
dictionaries = [dict_bi,dict_tri]

#TODO function that returns all the trigrams starting with given two words
""" OLD function
def wordGenerator(df, wordlist):
    lambda1 = 0.005
    lambda2 = 40.995
    lambda3 = 50
    flag2words = (len(wordlist)==2)
    print(flag2words)
    print(wordlist[0])
    #print(df[0])

    highscore = ('NaN', 0)

    for index, row in df[0].iterrows():
        freq_uni = row['frequency']
        # Leave out the scores of '[END]' and '[BEGIN]
        if (row['grams']=='[END]' or row['grams']=='[BEGIN]'):
            freq_uni = 0
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
    return highscore[0]
"""

""" OLD
def wordGenerator(df, dict, wordlist):
    lambda1 = 0.00005
    lambda2 = 0.5
    lambda3 = 5

    highscore = ('NaN', 0)

    for index, row in df[0].iterrows():
        freq_uni = row['frequency']
        word = row['grams']
        # Leave out the scores of '[END]' and '[BEGIN]
        if (word=='[END]' or word=='[BEGIN]'):
            freq_uni = 0
        freq_bi = dict[0].get(wordlist[0]+" "+word, 0)
        freq_tri = dict[1].get((wordlist[1]+" "+wordlist[0]+" "+word), 0)
        probability = lambda1*freq_uni+lambda2*freq_bi+lambda3*freq_tri
        if (probability > highscore[1]):
            highscore = (word,probability)
    return highscore[0]
"""

def wordGenerator(df, dict, wordlist):
    lambda1 = 10
    lambda2 = 100
    lambda3 = 100

    words = []
    words.append("NaN")
    probabilities = []
    probabilities.append(0)

    for index, row in df[0].iterrows():
        freq_uni = row['frequency']
        word = row['grams']
        # Leave out the scores of '[END]' and '[BEGIN]
        #if (word=='[END]' or word=='[BEGIN]'):
        #    freq_uni = 0
        freq_bi = dict[0].get(str(wordlist[0])+" "+str(word), 0)
        freq_tri = dict[1].get((str(wordlist[1])+" "+str(wordlist[0])+" "+str(word)), 0)
        probability = lambda1*freq_uni+lambda2*freq_bi+lambda3*freq_tri
        if probability>0.003:
            words.append(word)
            probabilities.append(np.exp(probability))
    #print(words)
    #print(softmax(probabilities))
    #print(words)
    #print(probabilities)
    #print(toProbability(probabilities))
    index = max(enumerate(probabilities),key=lambda x: x[1])[0]
    #return words[index]
    return np.random.choice(words, 1, p=softmax(probabilities))[0]

def toProbability(x):
    total = sum(x)
    for i in range(len(x)):
        x[i] = x[i]/total
    return x


"""
def softmax(x):
    Compute softmax values for each sets of scores in x.
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference
"""

def sentenceGenerator(df, dict,wdlist):
    sentence = wdlist
    i = 0
    #while not sentence[-1]=='[END]':
    for i in range(30):
        w = wordGenerator(df,dict,list(reversed(sentence[-2:])))
        #print(w)
        sentence.append(w)
        i +=1
    print(sentence)


def softmax(x):
    ex = np.exp(x)
    sum_ex = np.sum( np.exp(x))
    return ex/sum_ex

#sentence = ['thusrestrest','spake','test']
#print(list(reversed(sentence[-2:])))

#sentenceGenerator(grams_freq,dictionaries,['thus','spake'])
sentenceGenerator(grams_freq,dictionaries,['let','us','publish','some','books'])
#sentenceGenerator(grams_freq,dictionaries,['why','is'])
#sentenceGenerator(grams_freq,dictionaries,['can','you'])
#sentenceGenerator(grams_freq,dictionaries,['thus','spake'])

#wordGenerator(grams_freq, dictionaries, ["spake","thus"])
#wordGenerator(grams_freq,dictionaries,["do","what"])
#wordGenerator(grams_freq,dictionaries,["is","why"])
