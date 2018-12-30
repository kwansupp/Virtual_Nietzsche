with open('test_nietzsche.txt', 'r') as myfile:
    #test_sentence=myfile.read().replace('\n', '')
    for line in myfile:
        for word in line.split():
           print(word)

#print(test_sentence)

trigrams = [([test_sentence[i], test_sentence[i + 1]], test_sentence[i + 2])
            for i in range(len(test_sentence) - 2)]
# print the first 3, just so you can see what they look like
#print(trigrams[:3])
