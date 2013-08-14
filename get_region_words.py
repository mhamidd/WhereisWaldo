#script to get count of region words/tweet in training data 
import numpy as np
import pandas as pd
from reg_words_check import NEWordCounter
from AppalachiaWordCounter import AppalachiaWordCounter
from sklearn.base import BaseEstimator, clone
import csv
#import train and test sets
train_data = pd.read_csv('short_clean_train.csv')
test_data = pd.read_csv('short_test.csv')

#convert Tweets to objects
train_data.dtypes
train_data['Tweet'] = train_data['Tweet'].astype(object)

test_data.dtypes
test_data['Tweet'] = test_data['Tweet'].astype(object)

#define features
tweets = train_data.Tweet
test_tweets = test_data.Tweet

#run training tweets through region word counter
#get array of ratio of region words: total words
ne = NEWordCounter()
custom = ne.transform(tweets)
test_custom = ne.transform(test_tweets)

#reshape custom from one row with 50k values to one column with 50k values
customswap = np.swapaxes(custom, 0,1)
test_customswap = np.swapaxes(test_custom, 0, 1)


#save new england word ratio as csv
np.savetxt('ne_wordcount.csv', customswap)
np.savetxt('ne_wordcount_test.csv', test_customswap)

#onto Appalachia!
appalachia = AppalachiaWordCounter()
custom = appalachia.transform(tweets)
custom_test = appalachia.transform(test_tweets)
my_custom = open("appalachia_wordcount.csv", 'wb')
wr_custom = csv.writer(my_custom)
wr_custom.writerows(custom)
