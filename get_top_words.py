#script to get most frequent ngrams from regions
import numpy as np
import pandas as pd
import sys
from itertools import repeat
import csv

#load region data
filename = sys.argv[1]
train_data = pd.read_csv(filename)

#convert Tweet column to string for vectorizer
train_data.Tweet = str(train_data.Tweet) 

from sklearn.feature_extraction.text import CountVectorizer

#make vectorizer
#bigram_vectorizer = CountVectorizer (stop_words = 'english', ngram_range=(1, 2), token_pattern=r'\b\w+\b', max_features=100, min_df=1)

word_vectorizer = CountVectorizer (stop_words = 'english', token_pattern=r'\b\w+\b', max_features=100, min_df=1)


#text_features2 = bigram_vectorizer.fit_transform(train_data.Tweet)
text_features2 = word_vectorizer.fit_transform(train_data.Tweet)


#get feature names
#bigram_vectorizer.get_feature_names()
word_vectorizer.get_feature_names()

#word seems to work better
words = word_vectorizer.get_feature_names()


#save words to list
f = open(sys.argv[2], "w")
mylist = words
f.write("\n".join(map(lambda x: str(x), words)))
f.close()

