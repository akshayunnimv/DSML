print("SJC23MCA-2009 : AKSHAY UNNI M V")
print("Batch : MCA 2023-25")
from nltk import ngrams
sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)